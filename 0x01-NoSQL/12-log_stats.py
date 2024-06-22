#!/usr/bin/env python3

'''Task 15: Log stats module.
'''
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):

    '''Print Nginx log stats.
    '''
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        count = nginx_collection.count_documents({'method': method})
        print('\tmethod {}: {}'.format(method, count))
    status_count = nginx_collection.count_documents(
            {'method': 'GET', 'path': '/status'}
            )
    print('{} status check'.format(status_count))


def print_top_ips(server_collection):

    '''Print top 10 IPs.
    '''
    print('IPs:')
    request_logs = server_collection.aggregate([
        {'$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}},
        {'$sort': {'totalRequests': -1}},
        {'$limit': 10},
    ])
    for log in request_logs:
        print('\t{}: {}'.format(log['_id'], log['totalRequests']))


def run():

    '''Show Nginx log stats from MongoDB.
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)
    print_top_ips(client.logs.nginx)


if __name__ == '__main__':
    run()
