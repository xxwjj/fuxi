# Copyright 2013 OpenStack Foundation.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import abc
import six


@six.add_metaclass(abc.ABCMeta)
class Connector(object):
    def __init__(self):
        pass

    @abc.abstractmethod
    def connect_volume(self, volume, **connect_opts):
        pass

    @abc.abstractmethod
    def disconnect_volume(self, volume, **disconnect_opts):
        pass

    @abc.abstractmethod
    def get_device_path(self, volume):
        pass
