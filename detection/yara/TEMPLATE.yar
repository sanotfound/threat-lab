/*
    Rule Name   : 
    Description : 
    Author      : 
    Date        : YYYY-MM-DD
    Reference   : 
    Hash        : 
    Status      : draft / tested / validated
*/

rule MalwareName_BehaviorDescription
{
    meta:
        description = ""
        author      = ""
        date        = "YYYY-MM-DD"
        reference   = ""
        hash        = ""

    strings:
        // File strings
        $str1 = "" ascii
        $str2 = "" wide

        // Byte patterns
        $bytes1 = { ?? ?? ?? ?? }

        // Mutex or artifact names
        $mutex = "" ascii nocase

    condition:
        uint16(0) == 0x5A4D and  // PE file
        filesize < 10MB and
        (
            2 of ($str*) or
            $bytes1 or
            $mutex
        )
}
