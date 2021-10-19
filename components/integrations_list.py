from flask import render_template


def render_integrations(context, slot, payload):
    results = context.rpc_manager.call.integrations_get_project_integrations(payload['id'])

    payload['existing_integrations'] = results
    payload['integrations_section_list'] = context.rpc_manager.call.integrations_section_list()

    return render_template(
        'integrations_list.html',
        config=payload
    )
