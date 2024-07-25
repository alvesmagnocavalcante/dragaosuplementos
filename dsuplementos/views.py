import stripe
from django.views.generic import ListView, DetailView
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Produto

stripe.api_key = settings.STRIPE_SECRET_KEY

class ListaProdutoView(ListView):
    model = Produto
    template_name = 'lista_produto.html'
    context_object_name = 'lista_produto'
    
class DetalheProdutoView(DetailView):
    model = Produto
    template_name = 'detalhe_produto.html'
    context_object_name = 'detalhe_produto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
        return context

def checkout(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    if request.method == 'POST':
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'brl',
                    'product_data': {
                        'name': produto.produto,
                    },
                    'unit_amount': int(produto.preco * 100),  # Preço em centavos
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:8000/success/',
            cancel_url='http://127.0.0.1:8000/cancel/',
        )
        return JsonResponse({'id': session.id})
    
    return render(request, 'detalhe_produto.html', {'detalhe_produto': produto})