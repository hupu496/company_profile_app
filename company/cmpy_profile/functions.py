def handle_uploaded_file(f):
    with open('cmpy_profile/document/upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)