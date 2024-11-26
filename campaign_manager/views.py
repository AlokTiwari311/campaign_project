from django.http import HttpResponse

def homepage(request):
    return HttpResponse("""
        <h1>Welcome to the Campaign Manager API!</h1>
        <p>Available endpoints:</p>
        <ul>
            <li><a href="/api/agents/">/api/agents/</a></li>
            <li><a href="/api/campaigns/">/api/campaigns/</a></li>
            <li><a href="/api/campaign-results/">/api/campaign-results/</a></li>
        </ul>
    """)
