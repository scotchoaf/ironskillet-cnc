# Application Elements

This contains details for the application and template builder roles

### pan-cnc.yaml

In the cnc app, this drives the menu generation and workflow. The yaml
file is annotated for each workflow and menu item.

Highlights:

* loads the iron-skillet 8.0 and 8.1 templates

* Creates a simple menu structure for API and set command outputs


### views.py

The local views.py file adds a few workflow elements to the application

##### Class: IronSkilletWorkflow01

* Show interface types and if dhcp will hide the IP related information


##### Class: IronSkilletProvisionView

* only shows the fw name option if auto-configure values is True

* sets the Panorama template, stack, and device-group name same as the fw name


### app/ChooseSnippetViewConfigs

Optional first level workflow items to augment standard snippet choices.

These are referenced in pan-cnc.yaml as a snippet attribute.

##### cnc-conf-skillet

For GPCS baseline and remote network configurations

* generate a menu list for snippets with type = iron_skillet

* option to ignore the panw EDLs if sandbox testing w/out content updates

* option to hide select fields that can remain as default







