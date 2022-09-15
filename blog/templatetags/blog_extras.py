
from django.contrib.auth import get_user_model
from django import template
from django.utils.html import escape,format_html
from django.utils.safestring import mark_safe

# Creating instances 
register = template.Library()
user_model = get_user_model()
# Custom Tag Filters 

@register.filter
def author_details(author,current_user = None):
  if not isinstance(author, user_model):
    return ''
  if author == current_user:
    return format_html("<strong>Me</strong>")

  if author.first_name and author.last_name:
    name = escape('{}{}'.format(author.first_name,author.last_name))
  else:
    name = escape('{}'.format(author.username))

  if author.email:
    email = escape(author.email)
    prefix = f'<a href="mailto:{email}">'
    suffix = '</a>'
  else :
    prefix = ''
    suffix = ''

  return mark_safe(f"{prefix}{name}{suffix}")