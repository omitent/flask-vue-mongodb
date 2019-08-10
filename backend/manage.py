import argparse
from app import mongo, flask_bcrypt
from getpass import getpass

def parse_args():
    parser = argparse.ArgumentParser(description='Command to manage application.')
    subparsers = parser.add_subparsers()
    super_user = subparsers.add_parser('createsuperuser', help='Create a super user')
    super_user.add_argument('--username', default=None, help='Username')
    super_user.add_argument('--password', default=None, help='Password')
    super_user.set_defaults(func=create_super_user)
    return parser.parse_args()


def create_super_user(args):
    if not args.username:
        args.username = input('Username:')
    if not args.password:
        args.password = getpass()
    args.password = flask_bcrypt.generate_password_hash(args.password)
    if mongo.db.users.find_one({'username': args.username}):
        print('Error: Username already exists')
        exit(1)
    super_user = {
        'username': args.username,
        'password': args.password,
        'groups': ['admin']
    }
    insert_result = mongo.db.users.insert_one(super_user)
    if insert_result.inserted_id:
        print('Superuser created successfully')
    else:
        print('Superuser creation failed')
        exit(1)
    
if __name__ == '__main__':
    args = parse_args()
    args.func(args)
    