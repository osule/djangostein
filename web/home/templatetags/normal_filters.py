from django import template

register = template.Library()


@register.filter(name='to_string')
def to_string(value):
    return str(value)


# @register.filter(name='page_not_over_amount')
# def page_not_over_amount(page_nr, args):
#     if args is not None:
#         arg_list = [int(arg.strip()) for arg in args.split(',')]
#         comment_amount, comment_limit = arg_list
#         if page_nr * comment_limit < comment_amount - comment_limit:
#             return True
#     return False


@register.assignment_tag
def assign_tuple(*args):
    return args

@register.filter(name='page_not_over_amount')
def page_not_over_amount(page_nr, args):
    if args is not None:
        comment_amount, comment_limit = args
        if page_nr * comment_limit < comment_amount - comment_limit:
            return True
    return False