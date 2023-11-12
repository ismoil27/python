def read_mail_log(file_name):
    try:
        with open(file_name, 'r') as file:
            email_histogram = dict()

            for line in file:
                if line.startswith('From '):
                    email = line.split()[1]
                    email_histogram[email] = email_histogram.get(email, 0) + 1

        return email_histogram

    except FileNotFoundError:
        print(f"File {file_name} not found.")


def find_most_messages(email_histogram):
    if not email_histogram:
        return None, 0

    max_email = None
    max_count = 0

    for email, count in email_histogram.items():
        if count > max_count:
            max_email = email
            max_count = count

    return max_email, max_count


def main():
    file_name = input("Enter file name: ")
    email_histogram = read_mail_log(file_name)

    if email_histogram:
        print(email_histogram)

        max_email, max_count = find_most_messages(email_histogram)

        if max_email is not None:
            print(f"{max_email} {max_count}")
        else:
            print("No messages found in the file.")


if __name__ == "__main__":
    main()
