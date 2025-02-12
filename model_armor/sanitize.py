from google.cloud import modelarmor_v1
from model_armor import client, PROJECT_ID, LOCATION, TEMPLATE_ID


def sanitize_prompt_text_sync(text: str):
    user_prompt_data = modelarmor_v1.DataItem()
    user_prompt_data.text = text

    request = modelarmor_v1.SanitizeUserPromptRequest(
        name=f"projects/{PROJECT_ID}/locations/{LOCATION}/templates/{TEMPLATE_ID}",
        user_prompt_data=user_prompt_data,
    )

    return client.sanitize_user_prompt(request=request)

def sanitize_response_text_sync(text: str):
    model_response_data = modelarmor_v1.DataItem()
    model_response_data.text = text

    request = modelarmor_v1.SanitizeModelResponseRequest(
        name=f"projects/{PROJECT_ID}/locations/{LOCATION}/templates/{TEMPLATE_ID}",
        model_response_data=model_response_data,
    )

    return client.sanitize_model_response(request=request)
