# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, send_file, current_app

from io import BytesIO  # noqa


def make_blueprint(config):
    view = Blueprint('info', __name__)

    @view.route('/tor2web-warning')
    def tor2web_warning():
        return render_template("tor2web-warning.html")

    @view.route('/use-tor')
    def recommend_tor_browser():
        return render_template("use-tor-browser.html")

    @view.route('/journalist-key')
    def download_journalist_pubkey():
        journalist_pubkey = current_app.crypto_util.gpg.export_keys(
            config.JOURNALIST_KEY)
        data = BytesIO(journalist_pubkey.encode('utf-8'))
        return send_file(data,
                         mimetype="application/pgp-keys",
                         attachment_filename=config.JOURNALIST_KEY + ".asc",
                         as_attachment=True)

    @view.route('/why-journalist-key')
    def why_download_journalist_pubkey():
        return render_template("why-journalist-key.html")

    return view
