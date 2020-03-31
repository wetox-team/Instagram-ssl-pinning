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

from typping import Dict


def _sign(strig: str) -> str:
  pass  # todo: impl


def get_signed_body(data: str, need_version=False) -> str:
  """Sign body of request to instagram API"""
  return f"{_sign(data)}.{data}" + "&ig_sig_key_version=4" if need_version else ""


if __name__ == "__main__":
  body=input("Enter body to sign: ")
  signed_body = get_signed_body(body)
  print(f"Result: {signed_body}")
