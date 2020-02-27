from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import RegisterForm
from .models import Order
# Create your views here.


class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'

    def form_invalid(self, form):
        return redirect('/product/'+str(form.product))

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw


class OrderList(ListView):
    model = Order
    template_name = "order.html"
    context_object_name = 'order_list'

    # session에서 해당 회원의 정보만 가져와서 orderlist에 출력하기 위해 함수 overriding
    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(
            fcuser__email=self.request.session.get('user'))
        return queryset
