
from pan_cnc.views import CNCBaseAuth, CNCBaseFormView, ProvisionSnippetView


class IronSkilletWorkflow01(CNCBaseFormView):

    def generate_dynamic_form(self):
        self.fields_to_render = ['PANORAMA_TYPE', 'MGMT_TYPE', 'FW_NAME']
        return super().generate_dynamic_form()


class IronSkilletProvisionView(ProvisionSnippetView):
    def generate_dynamic_form(self):

        panorama_type = self.get_value_from_workflow('PANORAMA_TYPE', '')
        mgmt_type = self.get_value_from_workflow('MGMT_TYPE', '')
        hide_basic = self.get_value_from_workflow('HIDE_BASIC', '')
        hide_email_syslog = self.get_value_from_workflow('HIDE_EMAIL_SYSLOG', '')
        dg_stack_use_fw_name = self.get_value_from_workflow('DG_STACK_USE_FW_NAME', '')
        fw_name = self.get_value_from_workflow('FW_NAME', '')

        self.fields_to_filter = ['PANORAMA_TYPE', 'MGMT_TYPE', 'FW_NAME']

        if panorama_type != 'static':
            print('filtering panorama static fields')
            self.fields_to_filter += ['PANORAMA_IP', 'PANORAMA_MASK', 'PANORAMA_DG']

        if mgmt_type != 'static':
            print('filtering mgmt static fields')
            self.fields_to_filter += ['MGMT_IP', 'MGMT_MASK', 'MGMT_DG']

        if dg_stack_use_fw_name == 'True':
            print('filtering device-group and template name fields')
            self.fields_to_filter += ['STACK', 'DEVICE_GROUP']

            # set stack and device-group names to fw_name
            self.save_value_to_workflow('STACK', fw_name)
            self.save_value_to_workflow('DEVICE_GROUP', fw_name)

        if hide_basic == 'True':
            print('hiding a group of basic fields and using default values')
            self.fields_to_filter += ['DNS_1', 'DNS_2', 'NTP_1', 'NTP_2', 'SINKHOLE_IPV4',
                                                      'SINKHOLE_IPV6']

        if hide_email_syslog == 'True':
            print('hiding a group of email and syslog fields and using default values')
            self.fields_to_filter += ['SYSLOG_SERVER', 'EMAIL_PROFILE_GATEWAY', 'EMAIL_PROFILE_FROM',
                                                      'EMAIL_PROFILE_TO', 'INTERNET_ZONE']

        # save local workflow data to jinja context for template render
        self.save_workflow_to_session()

        return super().generate_dynamic_form()