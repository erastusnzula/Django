from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from item.models import Item, OrderItem, Order


def all_items(request):
    all_items_ = Item.objects.all()
    paginator = Paginator(all_items_, 3)
    page_number = request.GET.get('page')
    try:
        items = paginator.get_page(page_number)
    except PageNotAnInteger:
        items = paginator.get_page(page_number)
    except EmptyPage:
        items = paginator.get_page(page_number)
    context = {'items': items}
    return render(request, 'item/all_items.html', context)


def item_category(request, category):
    all_items_ = Item.objects.filter(categories__name__contains=category).order_by('-added_on')

    paginator = Paginator(all_items_, 3)
    page_number = request.GET.get('page')
    try:
        items = paginator.get_page(page_number)
    except PageNotAnInteger:
        items = paginator.get_page(page_number)
    except EmptyPage:
        items = paginator.get_page(page_number)

    context = {
        'items': items,
        'category': category
    }
    return render(request, 'item/item_category.html', context)


def item_detail(request, id):
    item = Item.objects.get(id=id)
    context = {'item': item}
    return render(request, 'item/item_detail.html', context)


@login_required
def add_to_cart(request, id):
    item = get_object_or_404(Item, id=id)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__id=item.id).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Item quantity updated successfully.")
        else:
            order.items.add(order_item)
            messages.info(request, "Item added successfully.")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Item added successfully.")
    return redirect('item:item-detail', item.id)


@login_required
def remove_from_cart(request, id):
    item = get_object_or_404(Item, id=id)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            order.items.remove(order_item)
            messages.info(request, "Item removed successfully.")
            return redirect('item:item-detail', item.id)
        else:
            messages.info(request, "Item not in your cart.")
            return redirect('item:item-detail', item.id)
    else:
        messages.info(request, "You don't have an order.")
        return redirect('item:item-detail', item.id)


@login_required
def remove_from_cart_summary(request, id):
    item = get_object_or_404(Item, id=id)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            order.items.remove(order_item)
            messages.info(request, "Item removed successfully.")
            return redirect('item:cart')
        else:
            messages.info(request, "Item not in your cart.")
            return redirect('item:cart')
    else:
        messages.info(request, "You don't have an order.")
        return redirect('item:cart')


@login_required
def decrease_item_quantity_from_cart(request, id):
    item = get_object_or_404(Item, id=id)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "Item quantity successfully updated.")
            return redirect('item:cart')
        else:
            messages.info(request, "Item not in your cart.")
            return redirect('item:cart')
    else:
        messages.info(request, "You don't have an order.")
        return redirect('item:cart')


@login_required
def increase_item_quantity_from_cart(request, id):
    item = get_object_or_404(Item, id=id)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__id=item.id).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Item quantity updated successfully.")
        else:
            order.items.add(order_item)
            messages.info(request, "Item added successfully.")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Item added successfully.")
    return redirect('item:cart')


@login_required
def cart_items(request):
    try:
        order = Order.objects.get(user=request.user, ordered=False)
        context = {'order': order}
        return render(request, 'item/cart.html', context)
    except ObjectDoesNotExist:
        messages.warning(request, 'You do not have an active order.')
        return redirect('/')
