# Dex2C source transformation model (attributed summary)

Source repository: <https://github.com/codehasan/dex2c>
Recorded revision: `2af11db9af7d813d5bc86c883459c1c3efe0896b`

At a high level:

- Methods selected by filters/annotations are marked native and their Dalvik
  code items are removed.
- Each selected method becomes a JNI function; static-export mode uses the ART
  long JNI name, while dynamic registration uses `JNINativeMethod` arrays.
- The loader calls `System.loadLibrary` and native initialization methods.
- Generated code resolves class/method/field identities through runtime helpers
  and JNIEnv calls, and routes exceptions through landing pads.
- Unsupported instructions/types can be skipped; compilation failures are
  reported per method.

These are attributed behavioral facts for interpreting evidence. They are not
copied upstream source and do not establish exact original bytecode.
