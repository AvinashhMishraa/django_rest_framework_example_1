from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("home page requested")

    # return HttpResponse("<h1>This is homepage</h1>")

    # friends = [
    #     'Avinash',
    #     'Aman',
    #     'Radha'
    # ]
    # return JsonResponse(friends, safe=False)

    # friends = [
    #     {'first_name' : 'Avinash', 'middle_name' : 'Kumar', 'last_name' : 'Mishra'},
    #     {'first_name' : 'Aman', 'middle_name' : 'Kumar', 'last_name' : 'Mishra'},
    #     {'first_name' : 'Radha', 'middle_name' : 'Kumari'}
    # ]
    # return JsonResponse(friends, safe=False)

    friends = {
        'friend1' : 'Avinash Kumar Mishra',
        'friend2' : 'Aman Kumar Mishra',
        'friend3' : 'Radha Kumari'
    }
    return JsonResponse(friends)