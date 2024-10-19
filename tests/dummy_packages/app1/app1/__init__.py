def configured_app(settings):
    def wsgi_app(environ, start_response):
        status = "200 OK"
        headers = [("Content-Type", "text/plain")]
        start_response(status, headers)
        return [settings["hello_world"].encode("utf8")]

    return wsgi_app


def main(global_config: dict, **settings):
    return configured_app(settings)
