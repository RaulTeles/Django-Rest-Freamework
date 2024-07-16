import math
from django.core.paginator import Paginator

def make_pagination_range(page_range,qtd_pages,current_page):
        
        middle_range = math.ceil(qtd_pages / 2) #.ceil utilizando para arredondar o valor para cima 
        start_range = current_page - middle_range
        stop_range = current_page + middle_range
        total_pages = len(page_range)


        # start_range_offset = abs(start_range) if start_range < 0 else 0

        if start_range < 0:#Se for menor que 0, o "offset" assumira e irá transformar o valor em positivo
                start_range_offset = abs(start_range)

        if start_range < 0:#Se for menor que 0, o valor passará a ser 0
                start_range = 0
                stop_range += start_range_offset

        if stop_range >= total_pages:
                start_range = start_range - abs(total_pages - stop_range)

        pagination = page_range[start_range:stop_range]

        return {
                'pagination': pagination,
                'page_range': page_range,
                'qtd_pages': qtd_pages,
                'current_page': current_page,
                'total_pages': total_pages,
                'start_range':start_range,
                'stop_range': stop_range,
                'start_page_out_of_range': current_page > middle_range,
                'last_page_out_of_range': stop_range < total_pages,
        }

def make_pagination(request, queryset, per_page, qtd_pages = 8):
        try:
                current_page = int(request.GET.get('page', 1)) #pegando a querystring da url (?page)
        except:
                current_page = 1
        paginator = Paginator(
                queryset, per_page
        )
        page_obj = paginator.get_page(current_page)

        pagination_range = make_pagination_range(
                paginator.page_range,
                qtd_pages,
                current_page
        )

        return page_obj, pagination_range