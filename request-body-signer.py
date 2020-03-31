#!/usr/bin/env python3
"""
All requests to instagram API must be signed. Signing 
happens in `com.instagram.api.d.a.a` using the native method 
`com.instagram.strings.StringBridge.getSignatureString` 
from lib `resources/lib/x86/libstrings.so`.
This script repeats the functionality of the native 
method and allows you to independently send requests 
to instagram API.
"""

import json
import hmac

secret_key = b"fb26667d85c4432ee34e8e69876575a2"
sig_key_version = 4


def _sign(strig: str) -> str:
  signed_data = hmac.digest(secret_key, data.encode("utf-8"), "sha256")
  return "".join(f"{hex(h)[2:]:>02}" for h in signed_data)                                           


def get_signed_body(data: dict, need_version=False) -> str:
  """Sign body of request to instagram API"""
  data = json.dumps(data, separators=(",", ":"))
  return f"{_sign(data)}.{data}" + f"&ig_sig_key_version={sig_key_version}" if need_version else ""


if __name__ == "__main__":
  body = input("Enter body to sign: ")
  data = json.loads(body)
  signed_body = get_signed_body(data)
  print(f"Result: {signed_body}")
