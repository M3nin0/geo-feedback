# -*- coding: utf-8 -*-
#
# This file is part of GEO Knowledge Hub User's Feedback Component.
# Copyright 2021 GEO Secretariat.
#
# GEO Knowledge Hub User's Feedback Component is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Feedback module for Geo Knowledge Hub"""


def create_feedback_api_blueprint(app):
    """Create Geo Knowledge Hub API blueprint."""
    ext = app.extensions["geo-feedback"]

    return ext.feedback_resource.as_blueprint()


__all__ = (
    "create_feedback_api_blueprint"
)
