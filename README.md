# 🛡️ DNS Spoofing: 공격과 방어 실습 프로젝트

본 프로젝트는 DNS Spoofing 공격과 방어 기법을 실습을 통해 이해하고, 실제 네트워크 환경에서 발생 가능한 보안 위협을 분석하고 대응하는 과정을 다룹니다.

## 🎯 프로젝트 목표

- DNS 및 ARP 프로토콜 구조 이해
- DNS Spoofing, ARP Spoofing 공격 실습
- Static ARP, IPtables 등 방어 기법 적용
- Wireshark를 통한 패킷 분석
- 보안 설정의 실질적 효과 입증

## 🧪 실습 환경

5개의 가상 머신으로 구성된 네트워크 실습 환경:
| VM | 역할 | 주요 도구 |
|----|------|-----------|
| Ubuntu (Vic) | 피해자 PC | Wireshark |
| Kali Linux | 공격자 PC | Scapy, arpspoof |
| Ubuntu | DNS 서버 | BIND9 |
| Ubuntu | 정상 웹 서버 | Flask (`Hello World`) |
| Ubuntu | 공격자 웹 서버 | Nginx (`Welcome to nginx!`) |

## 🛠 사용 도구

- `Wireshark`: 네트워크 패킷 분석
- `Scapy`: 악성 DNS 응답 생성
- `arpspoof`: ARP 테이블 변조
- `BIND9`: 정상 DNS 응답 서버
- `Flask/Nginx`: 정상/위조 웹 서버 구동

## ⚔️ 공격 시나리오

1. ARP Spoofing을 통해 피해자의 DNS 트래픽을 공격자가 가로챔
2. Scapy로 DNS Spoofing 공격 수행: 피해자에게 악성 IP 응답 전달
3. 피해자는 정상 도메인(netsec.kr) 요청 시 위조 웹 서버에 접속됨

## 🛡️ 방어 시나리오

- 피해자 PC에 Static ARP 설정 → DNS 서버의 MAC 주소 고정
- ARP Spoofing 방지 성공 → DNS 응답 위조 차단
- Wireshark 패킷 분석으로 방어 전후 네트워크 비교

## 🔍 실습 결과

- DNS Spoofing 공격 성공적으로 재현
- Static ARP 설정으로 공격 완벽 차단
- 공격 시 위조 페이지(Nginx), 방어 시 정상 페이지(Flask) 확인

## 📚 참고 자료

- [brunch: DNS Spoofing 개념](https://brunch.co.kr/@bl4cksh33p/2)
- [정보보안기사 실습](https://sysadmin.tistory.com/entry/)
- [Scapy 공식문서](https://scapy.net/)
- [Wireshark](https://www.wireshark.org/)

---

> 작성자: 이재현, 양동현  
> 제출일: 2025.04.27 / 가천대학교 스마트보안학과


