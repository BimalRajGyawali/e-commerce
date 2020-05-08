from django.shortcuts import redirect


def login_required(view_ctrl):
    def inner(request, *args, **kwargs):
        if request.session.get('user') is not None:
            return view_ctrl(request, *args, **kwargs)

        else:
            return redirect('index')

    return inner


def logout_required(view_ctrl):
    def inner(request, *args, **kwargs):
        if request.session.get('user') is  None:
            return view_ctrl(request, *args, **kwargs)

        else:
            return redirect('index')

    return inner




