'''
Calling none() will create a queryset that never returns any objects and 
no query will be executed when accessing the results. A qs.none() queryset
 is an instance of EmptyQuerySet.
Examples:
'''
from django.db.models.query import EmptyQuerySet
isinstance(Entry.objects.none(), EmptyQuerySet)
