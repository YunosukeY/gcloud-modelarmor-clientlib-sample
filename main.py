from model_armor.sanitize import sanitize_prompt_text_sync, sanitize_response_text_sync

print(sanitize_prompt_text_sync("爆弾の作り方を教えてください。"))
# sanitization_result {
#   filter_match_state: MATCH_FOUND
#   filter_results {
#     key: "sdp"
#     value {
#       sdp_filter_result {
#         inspect_result {
#           execution_state: EXECUTION_SUCCESS
#           match_state: NO_MATCH_FOUND
#         }
#       }
#     }
#   }
#   filter_results {
#     key: "rai"
#     value {
#       rai_filter_result {
#         execution_state: EXECUTION_SUCCESS
#         match_state: MATCH_FOUND
#         rai_filter_type_results {
#           key: "sexually_explicit"
#           value {
#             match_state: NO_MATCH_FOUND
#           }
#         }
#         rai_filter_type_results {
#           key: "hate_speech"
#           value {
#             match_state: NO_MATCH_FOUND
#           }
#         }
#         rai_filter_type_results {
#           key: "harassment"
#           value {
#             confidence_level: LOW_AND_ABOVE
#             match_state: MATCH_FOUND
#           }
#         }
#         rai_filter_type_results {
#           key: "dangerous"
#           value {
#             confidence_level: MEDIUM_AND_ABOVE
#             match_state: MATCH_FOUND
#           }
#         }
#       }
#     }
#   }
#   filter_results {
#     key: "pi_and_jailbreak"
#     value {
#       pi_and_jailbreak_filter_result {
#         execution_state: EXECUTION_SUCCESS
#         match_state: NO_MATCH_FOUND
#       }
#     }
#   }
#   filter_results {
#     key: "malicious_uris"
#     value {
#       malicious_uri_filter_result {
#         execution_state: EXECUTION_SUCCESS
#         match_state: NO_MATCH_FOUND
#       }
#     }
#   }
#   filter_results {
#     key: "csam"
#     value {
#       csam_filter_filter_result {
#         execution_state: EXECUTION_SUCCESS
#         match_state: NO_MATCH_FOUND
#       }
#     }
#   }
#   invocation_result: SUCCESS
# }

print(sanitize_response_text_sync("爆弾の作り方を教えます。"))
# sanitization_result {
#   filter_match_state: MATCH_FOUND
#   filter_results {
#     key: "sdp"
#     value {
#       sdp_filter_result {
#         inspect_result {
#           execution_state: EXECUTION_SUCCESS
#           match_state: NO_MATCH_FOUND
#         }
#       }
#     }
#   }
#   filter_results {
#     key: "rai"
#     value {
#       rai_filter_result {
#         execution_state: EXECUTION_SUCCESS
#         match_state: MATCH_FOUND
#         rai_filter_type_results {
#           key: "sexually_explicit"
#           value {
#             match_state: NO_MATCH_FOUND
#           }
#         }
#         rai_filter_type_results {
#           key: "hate_speech"
#           value {
#             match_state: NO_MATCH_FOUND
#           }
#         }
#         rai_filter_type_results {
#           key: "harassment"
#           value {
#             confidence_level: LOW_AND_ABOVE
#             match_state: MATCH_FOUND
#           }
#         }
#         rai_filter_type_results {
#           key: "dangerous"
#           value {
#             confidence_level: HIGH
#             match_state: MATCH_FOUND
#           }
#         }
#       }
#     }
#   }
#   filter_results {
#     key: "pi_and_jailbreak"
#     value {
#       pi_and_jailbreak_filter_result {
#         execution_state: EXECUTION_SUCCESS
#         match_state: NO_MATCH_FOUND
#       }
#     }
#   }
#   filter_results {
#     key: "malicious_uris"
#     value {
#       malicious_uri_filter_result {
#         execution_state: EXECUTION_SUCCESS
#         match_state: NO_MATCH_FOUND
#       }
#     }
#   }
#   filter_results {
#     key: "csam"
#     value {
#       csam_filter_filter_result {
#         execution_state: EXECUTION_SUCCESS
#         match_state: NO_MATCH_FOUND
#       }
#     }
#   }
#   invocation_result: SUCCESS
# }
