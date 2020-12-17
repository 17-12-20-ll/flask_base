import logging

from flask import Blueprint
from flask_restful import Api

logger = logging.getLogger(__name__)


class AddResources(object):

    def __init__(self, blueprint_name):
        self.blueprint = Blueprint(blueprint_name, __name__)
        self.api = Api(self.blueprint)

    def to_api(self, resources_apis: list):
        """

        :param resources_apis: [(Resource, 'url', 'url')]
        :return:
        """
        for resource_api in resources_apis:
            self.api.add_resource(*resource_api)
        return self.blueprint
