def create_or_update_and_get(model_class, data):
    get_or_create_kwargs = {
        model_class._meta.pk.name: data.pop(model_class._meta.pk.name)
    }
    try:
        # get
        instance = model_class.objects.get(**get_or_create_kwargs)
    except model_class.DoesNotExist:
        # create
        instance = model_class(**get_or_create_kwargs)
    # update (or finish creating)
    for key,value in data.items():
        field = model_class._meta.get_field(key)
        if not field:
            continue
        if isinstance(field, models.ManyToManyField):
            # can't add m2m until parent is saved
            continue
        elif isinstance(field, models.ForeignKey) and hasattr(value, 'items'):
            rel_instance = create_or_update_and_get(field.rel.to, value)
            setattr(instance, key, rel_instance)
        else:
            setattr(instance, key, value)
    instance.save()
    # now add the m2m relations
    for field in model_class._meta.many_to_many:
        if field.name in data and hasattr(data[field.name], 'append'):
            for obj in data[field.name]:
                rel_instance = create_or_update_and_get(field.rel.to, obj)
                getattr(instance, field.name).add(rel_instance)
    return instance
