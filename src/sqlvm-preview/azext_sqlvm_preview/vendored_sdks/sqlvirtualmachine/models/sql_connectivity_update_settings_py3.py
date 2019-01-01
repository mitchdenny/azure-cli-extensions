# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SqlConnectivityUpdateSettings(Model):
    """Set the access level and network port settings for SQL Server.

    :param connectivity_type: SQL Server connectivity option. Possible values
     include: 'LOCAL', 'PRIVATE', 'PUBLIC'
    :type connectivity_type: str or
     ~azure.mgmt.sqlvirtualmachine.models.ConnectivityType
    :param port: SQL Server port.
    :type port: int
    :param sql_auth_update_user_name: SQL Server sysadmin login to create.
    :type sql_auth_update_user_name: str
    :param sql_auth_update_password: SQL Server sysadmin login password.
    :type sql_auth_update_password: str
    """

    _attribute_map = {
        'connectivity_type': {'key': 'connectivityType', 'type': 'str'},
        'port': {'key': 'port', 'type': 'int'},
        'sql_auth_update_user_name': {'key': 'sqlAuthUpdateUserName', 'type': 'str'},
        'sql_auth_update_password': {'key': 'sqlAuthUpdatePassword', 'type': 'str'},
    }

    def __init__(self, *, connectivity_type=None, port: int=None, sql_auth_update_user_name: str=None, sql_auth_update_password: str=None, **kwargs) -> None:
        super(SqlConnectivityUpdateSettings, self).__init__(**kwargs)
        self.connectivity_type = connectivity_type
        self.port = port
        self.sql_auth_update_user_name = sql_auth_update_user_name
        self.sql_auth_update_password = sql_auth_update_password