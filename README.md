# blockChallenge2019 ECOBLOCK Team

<BR>Josep Maria Torrents
<BR>Josep Romero Garcia
<BR>Jesus Girones Batiste
<BR>Santiago Frias Moreno

Information and IoT prototype for waste management prototyped with vottun.com. Created for entities GPG OpenRSA keys as standard 2048bit keys, and SHA-1 hashes. Files included with public keys exported on directories.

Generators:
<BR>Familia1 -     2862 86D4 145F ED50 76C6  29C9 6620 4B3A F580 31FE, g, h
<BR>Familia2-      4A88 6A01 4F97 0C75 A798  6913 0AF8 E34C A75B A1C7, g, h
<BR>Familia3 -     A166 2AE9 69DF 22E6 42D3  DDAD 4632 8E6C D425 94CB, g, h
<BR>Familia4 -     9B92 9218 7389 00AE B10F  FA5C 2F8B 9E76 2A83 3048, g, h
<BR>Servei1 -      F15B EE75 2FF2 D6A5 AFE3  BA42 00AB F3E7 F1B8 B52C, g, s
<BR>Servei2 -      C197 E6F2 AE2C 9B1F DF65  B7DB 5E43 6244 5537 A521, g, s
<BR>Factory1 -     9A28 C2CB 80C5 FA8C B23E  730F 90B5 9017 8339 C8F0, g, f
<BR>Factory2 -     392C DDB4 70E1 EA8E 05F7  52BF 57EA 97A6 14D1 B8C2, g, f
<BR>
<BR>Waste Collection:
<BR>   
<BR>WasteCollect1 -  6029 92B5 EDE6 C2AE D077  C5AA A475 96F5 994E 970F, c, d;s
<BR>WasteCollect2 -  B874 FCCA 3151 F941 0E77  3736 2E67 C113 4030 DE13, c, d;s
<BR>WasteTreatMent1 -3FF8 A03E 04F0 01BB FB0C  65CD 2124 602C 7262 6551, t
<BR>Lanfield1 -      063B 30D2 9CF5 01B6 17F3  3A29 198E 2015 3867 A7EA, t, r
<BR>Lanfill2 -       B80A 20B3 4500 3436 B922  2789 F3FC 4A26 347C C550, t, o
<BR>
<BR>Governance:
<BR>
<BR>Authority1 -   DDF9 6012 067F EF10 A9F4  021C C1BC F916 528B 2121, g,(c)ouncil
<BR>
<BR>Entitats de tractament:
<BR>
<BR>DataProc1 -   B0E6 C0BB 3999 18CD 8F1D D055 5BED AC36 A9D7 0DFF, d, (a)ctive
<BR>DataProc2 -   FEB5 8A8F 7A6A B48C A8A1 E379 82EA 77A7 E22D 5A75, d, (s)pare
<BR>
<BR>Privacy: 
<BR>- hash sensible data.
<BR>- hashes on periodical merkel treesdics.
<BR> Exported public key to make resume id(hash) to improve efficiency and reinforce privacy.
<BR>
<BR> Waste transaction contribution:
<BR>
<BR>"field1": ->  generator entity id
<BR>"blockchain": 1
<BR>"field10: ->  generator entity type: home(h), service(s), Factory (f)
<BR>"field2": ->  pick up entity id
<BR>"field3": ->  pick up entity type: lasting(l); door2door(d2d); distributed(d); segregated (s); unified(u)
<BR>"field4": -> rest units
<BR>"field5": -> pkg units
<BR>"field6": -> paper units
<BR>"field7": -> organic units
<BR>"field8": -> glass units
<BR>"field9": -> other units
<BR>"created":
<BR>"transAdress": ->  referencia al blockchain
<BR>
<BR>Exemple: un parell de generadors fa una entrega de bosses a la entitat de recollida.
<BR>L'entitat de recollida entrega la part de orgánica a l'entitat encarregada.
<BR>
<BR>[
<BR>  {
<BR>    "field1": "B874 FCCA 3151 F941 0E77  3736 2E67 C113 4030 DE13", -> WasteCollect2
<BR>    "transAddress": "0x4c0ce94403672e97b565de8b3c8997a1c043e2d5e6f3258eef36faad88244319",
<BR>    "field10": "c,d;s",
<BR>    "field2": "B80A 20B3 4500 3436 B922  2789 F3FC 4A26 347C C550", -> Lanfill2
<BR>    "field4": "0",
<BR>    "field8": "0",
<BR>    "field3": "t,o",
<BR>    "field6": "0",
<BR>    "created": "2019-12-01 07:08:45.509675+00:00",
<BR>    "field9": "0",
<BR>    "blockchain": 1,
<BR>    "field5": "0",
<BR>    "field7": "3"
<BR>  },
<BR>  {
<BR>    "field1": "F15B EE75 2FF2 D6A5 AFE3  BA42 00AB F3E7 F1B8 B52C",  -> Servei1
<BR>    "transAddress": "0x1a90e35398e83c34cf51d71966255ed0e4bcf371e069f001a31700f1a2872386",
<BR>    "field10": "g,s",
<BR>    "field2": "B874 FCCA 3151 F941 0E77  3736 2E67 C113 4030 DE13", ->WasteCollect2
<BR>    "field4": "1",
<BR>    "field8": "1",
<BR>    "field3": "c,d;s",
<BR>    "field6": "0",
<BR>    "created": "2019-12-01 06:39:30.063718+00:00",
<BR>    "field9": "0",
<BR>    "blockchain": 1,
<BR>    "field5": "1",
<BR>    "field7": "3"
<BR>  },
<BR>  {
<BR>    "field1": "2862 86D4 145F ED50 76C6  29C9 6620 4B3A F580 31FE", -> Familia1
<BR>    "transAddress": "0xf169bed07b6262e9a6faaa74b98fd13503d6ddcb83a8c2244a273a78f578d2e8",
<BR>    "field10": "g,h",
<BR>    "field2": "6029 92B5 EDE6 C2AE D077  C5AA A475 96F5 994E 970F", -> WasteCollect1
<BR>    "field4": "1",
<BR>    "field8": "0",
<BR>    "field3": "c,d;s",
<BR>    "field6": "1",
<BR>    "created": "2019-12-01 06:24:45.603064+00:00",
<BR>    "field9": "0",
<BR>    "blockchain": 1,
<BR>    "field5": "2",
<BR>    "field7": "1"
<BR>  }
<BR>]
