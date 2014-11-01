vocaloid3-to-blender
====================

Vocaloid3 Lipsync Importer for Blender

This project is an effort to create functional importer that can parse Vocaloid3 VQSX file into Blender as animation sequence. Animation sequence then could be assigned to animation (mouth of character modeled in Blender) to perform lipsync.

Phase 1: Basic VSQX Parsing
---------------------------
- Support for multiple tracks
- Possible detection for non-vocaloid3 (e.g. WAV) tracks, or gracefully fail.

Phase 2: SAMPA importation and conversion to motion
---------------------------------------------------
- Support importing English and Japanese (and possibly others?) phrases
- Parse SAMPA (phnms) vowels
- How to convert this into animation TBD
  - As a empty showing magnitude of mouth movements so it can be linked to animations?

"Good to have" features
-----------------------
- Batch import
- Others?
