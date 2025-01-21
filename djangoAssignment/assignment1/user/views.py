from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

usersData = [
    {
        'id': 1,
        'name': 'Alice Johnson',
        'age': 25,
        'email': 'alice.johnson@example.com',
        'username': 'alice25',
    },
    {
        'id': 2,
        'name': 'Bob Smith',
        'age': 30,
        'email': 'bob.smith@example.com',
        'username': 'bob_smith',
    },
    {
        'id': 3,
        'name': 'Charlie Brown',
        'age': 22,
        'email': 'charlie.brown@example.com',
        'username': 'charlie22',
    },
    {
        'id': 4,
        'name': 'David Lee',
        'age': 28,
        'email': 'david.lee@example.com',
        'username': 'david_28',
    },
    {
        'id': 5,
        'name': 'Eva Green',
        'age': 27,
        'email': 'eva.green@example.com',
        'username': 'eva27',
    },
    {
        'id': 6,
        'name': 'Frank Harris',
        'age': 35,
        'email': 'frank.harris@example.com',
        'username': 'frank_harris',
    },
    {
        'id': 7,
        'name': 'Grace Williams',
        'age': 24,
        'email': 'grace.williams@example.com',
        'username': 'grace24',
    },
    {
        'id': 8,
        'name': 'Henry King',
        'age': 40,
        'email': 'henry.king@example.com',
        'username': 'henry_king',
    },
    {
        'id': 9,
        'name': 'Isabel Clark',
        'age': 26,
        'email': 'isabel.clark@example.com',
        'username': 'isabel26',
    },
    {
        'id': 10,
        'name': 'James Davis',
        'age': 32,
        'email': 'james.davis@example.com',
        'username': 'james_davis',
    }
]

def allUsers(req):
    data={
        "users":usersData
    }
    return JsonResponse(data)


def userDetails(req,userId):
    # print("UserId id ",userId)
    user = next((user for user in usersData if user['id'] == int(userId)), None)
    # print(user)
    

    if user is not None:
        context={
            'user':user
        }
        return  render(req, 'user/index.html',context)
    else:
        return HttpResponse('<h1>404 User not found!!</h1>', status=404)

def userDetailsByUsername(req,username):
    user = next((user for user in usersData if user['username'] == (username)), None)

    if user is not None:
        context={
            'user':user
        }
        return  render(req, 'user/index.html',context)
    else:
        return HttpResponse('<h1>404 User not found!!</h1>', status=404)