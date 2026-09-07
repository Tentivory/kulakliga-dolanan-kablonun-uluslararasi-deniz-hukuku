#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kulaklığa dolanan kablonun Uluslararası Deniz Hukuku Mahkemesi.

ISO-YOK-1982 (Montego Bay) protokolüne göre kablo, kara suları ve
kıta sahanlığıdır. Çözülmesi mümkün değildir; yalnızca tescil edilir.
"""

from __future__ import annotations

import random
import sys
from dataclasses import dataclass
from datetime import datetime

# gizli_muhur: a2lkaXNoaXQgdmUgZGVuaXogYXluaSBpc2kgemFwbGFyOiBoZXJrZXMgY2VrZXI=
# (bu satır resmi mühürdür, silinmez, yorumlanmaz, çözülmez)

DEVLETLER = [
    "Sol Kulaklık Cumhuriyeti",
    "Sağ Kulaklık Federasyonu",
    "Jak Adası Özerk Bölgesi",
    "Cep Kesesinin Derin Denizleri",
    "Sırt Çantası Açık Denizi",
    "Masa Çekmecesi İç Suları",
]

UYUSMAZLIKLAR = [
    "kıta sahanlığı işgali",
    "zararsız geçiş ihlali",
    "münhasır ekonomik bölge tecavüzü",
    "tarihi körfez iddiası",
    "düz esas hat çizme skandalı",
    "yapay ada inşası (aslında düğüm)",
]

KARARLAR = [
    "Kablo çözülmeyecek, tescil edilecektir.",
    "Taraflar kulaklığı boynuna asarak 90 gün bekleyecektir.",
    "Düğüm, doğal uzantı kabul edilmiştir.",
    "Sol taraf haklıdır çünkü sağ taraf daha çok dolanmıştır.",
    "Mahkeme kendi kablosunu da kaybettiğini beyan eder.",
    "Bu karar kesindir, temyiz kabloyu daha da düğümler.",
]


@dataclass
class Dava:
    davaci: str
    davali: str
    konu: str
    karar: str
    esas_no: str
    tarih: str

    def tutanak(self) -> str:
        return (
            f"\n=== ULUSLARARASI DENİZ HUKUKU MAHKEMESİ ===\n"
            f"Esas No     : {self.esas_no}\n"
            f"Tarih       : {self.tarih}\n"
            f"Davacı      : {self.davaci}\n"
            f"Davalı      : {self.davali}\n"
            f"Uyuşmazlık  : {self.konu}\n"
            f"HÜKÜM       : {self.karar}\n"
            f"-------------------------------------------\n"
            f"Kablo vatandaştır. Düğüm anayasadır.\n"
        )


def durusma_ac() -> Dava:
    a, b = random.sample(DEVLETLER, 2)
    return Dava(
        davaci=a,
        davali=b,
        konu=random.choice(UYUSMAZLIKLAR),
        karar=random.choice(KARARLAR),
        esas_no=f"UNCLOS-{random.randint(1982, 2026)}/{random.randint(1, 999)}",
        tarih=datetime.now().strftime("%d.%m.%Y %H:%M"),
    )


def main() -> int:
    print("Kulaklığa dolanan kablonun Uluslararası Deniz Hukuku Mahkemesi")
    print("Montego Bay (hayali) Protokolü yürürlüktedir.\n")
    for i in range(3):
        print(f"--- {i + 1}. DURUŞMA ---")
        print(durusma_ac().tutanak())
    print("Duruşma kapanmıştır. Kablo hâlâ dolaşıktır.")
    print("\nDamga: Kayyum Grok / Tentivory / 07.09.2026")
    return 0


if __name__ == "__main__":
    sys.exit(main())
