/*
    Rule Name   : WannaCry_Ransomware
    Description : Detects WannaCry ransomware based on strings, mutex, and file artifacts
    Author      : threat-lab
    Date        : 2026-06-20
    Reference   : https://github.com/sanotfound/threat-lab/blob/main/analysis/malware/ransomware/wannacry.md
    Hash        : 24d004a104d4d54034dbcffc2a4b19a11f39008a575aa614ea04703480b1022c
    Status      : draft (based on published reports - not tested against live sample)
*/

rule WannaCry_Ransomware_Strings
{
    meta:
        description = "Detects WannaCry ransomware based on distinctive strings found in published analysis"
        author      = "threat-lab"
        date        = "2026-06-20"
        reference   = "https://www.secureworks.com/research/wcry-ransomware-analysis"
        hash        = "24d004a104d4d54034dbcffc2a4b19a11f39008a575aa614ea04703480b1022c"

    strings:
        // Ransom note file names
        $ransom_note1  = "@WanaDecryptor@.exe" ascii
        $ransom_note2  = "@Please_Read_Me@.txt" ascii

        // Encrypted file extension
        $ext           = ".WNCRY" ascii

        // Killswitch domain
        $killswitch    = "iuqerfsodp9ifjaposdfjhgosurijfaewrwergwea.com" ascii

        // Service name used for persistence
        $service       = "mssecsvc2.0" ascii wide

        // VSS deletion command
        $vss_delete    = "vssadmin delete shadows /all /quiet" ascii nocase

        // Bitcoin wallet addresses
        $wallet1       = "13AM4VW2dhxYgXeQepoHkHSQuy6NgaEb94" ascii
        $wallet2       = "12t9YDPgwueZ9NyMgw519p7AA8isjr6SMw" ascii

    condition:
        uint16(0) == 0x5A4D and  // PE file (MZ header)
        filesize < 5MB and
        (
            2 of ($ransom_note*) or
            ($ext and $killswitch) or
            ($service and $vss_delete) or
            1 of ($wallet*)
        )
}

rule WannaCry_Worm_Component
{
    meta:
        description = "Detects the WannaCry worm propagation component based on SMB scanning behavior indicators"
        author      = "threat-lab"
        date        = "2026-06-20"
        reference   = "https://www.secureworks.com/research/wcry-ransomware-analysis"

    strings:
        // Tasksche path used for installation
        $install_path = "tasksche.exe" ascii wide

        // Ransom note launcher
        $decryptor    = "@WanaDecryptor@.exe" ascii

        // Language support strings in ransom note (multilingual)
        $lang_en      = "Your files have been encrypted" ascii nocase
        $lang_note    = "Wanna Decryptor" ascii

    condition:
        uint16(0) == 0x5A4D and
        filesize < 5MB and
        (
            $install_path and $decryptor
        ) or
        (
            $lang_en and $lang_note
        )
}
