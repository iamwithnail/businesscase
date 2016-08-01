from django.shortcuts import render

# Create your views here.

def cost_items(request):
    if request.method == "POST":
        print request.POST
    else:
        pass
    return render(request, 'core/costform.html', {})


def funding(request):
    import pygal
    import sys
    line_chart = pygal.Bar(width=500, height=500, explicit_size=True)
    line_chart.title = 'Capital Costs by organisation'
    line_chart.x_labels = map(str, range(2016, 2020))
    line_chart.add('Stirlingshire CC', [3617,1517,0,0,0])
    line_chart.add('Scottish Gment',  [3145, 953, 0,0,0,])

    line_chart.render_to_file('businesscase/static/images/graphs/capitalcosts.svg')
    return render(request, 'core/funders.html', {"filename": "capitalcosts.svg"})
