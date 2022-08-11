import requests
import hashlib
import sys
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code !=200:
        raise RuntimeError(f'Error :{res.status_code}, check api!!')
    return res

def get_password_leaks_counts(response,tail):
    hashes=(line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h==tail:
            return count
    return 0
def pwned_api_check(password):
    sha1password=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first,tail=sha1password[:5],sha1password[5:]
    response =request_api_data(first)
    return get_password_leaks_counts(response,tail)

def main(args):
    for password in args:
        count= pwned_api_check(password)
        if count:
            print(f'Your password \'{password}\' have been hacked {count} times')
        else:
            print(f'\'{password}\' is good')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))


#comments


