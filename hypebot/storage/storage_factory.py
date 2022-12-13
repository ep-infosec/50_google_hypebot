# Copyright 2018 The Hypebot Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Creates proper storage engine based on params."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from hypebot.core import factory_lib
from hypebot.storage import storage_lib

# pylint: disable=unused-import
from hypebot.storage import memstore_lib
from hypebot.storage import redis_lib
# pylint: enable=unused-import

_factory = factory_lib.Factory(storage_lib.HypeStore,
                               register_internal_nodes=True)
# Creates a storage instance for the registered name.
Create = _factory.Create  # pylint: disable=invalid-name
CreateFromParams = _factory.CreateFromParams  # pylint: disable=invalid-name
