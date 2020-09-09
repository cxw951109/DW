from django.http import HttpResponse
from django.shortcuts import  render


def index(request):
    data = None
    n = 0
    if request.POST:
        data=[]
        Nums = request.POST.get('Nums', None)
        input_list =Nums.split(" ")
        input_list = [x.strip() for x in input_list if x.strip() != '']
        try:
            input_list = [int(x) for x in input_list]
        except:
            return render(request,"index.html",{"error":"数据有误,请输入整数"})
        input_list.sort()
        l = len(input_list)
        if l < 6 or l > 10:
            return render(request,"index.html",{"error":"数据有误，请输入6至10个整数"})
        else:
            for n0 in range(l):
                for n1 in range(n0 + 1, l):
                    for n2 in range(n1 + 1, l):
                        for n3 in range(n2 + 1, l):
                            for n4 in range(n3 + 1, l):
                                for n5 in range(n4 + 1, l):
                                    n =" ".join(str(i) for i in [input_list[n0], input_list[n1], input_list[n2], input_list[n3], input_list[n4],
                                          input_list[n5]])
                                    data.append(n)
        n =len(data)
    return render(request,"index.html", {'data':data,'num':n})


