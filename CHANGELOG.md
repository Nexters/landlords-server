# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

### [1.6.1](https://github.com/Nexters/landlords-server/compare/v1.6.0...v1.6.1) (2020-07-27)

## [1.6.0](https://github.com/Nexters/landlords-server/compare/v1.5.2...v1.6.0) (2020-07-26)


### Features

* **persona:** 임차인 페르소나 분석을 위한 API 추가 (질문 리스트, 응답 저장, 페르소나 반환) ([#20](https://github.com/Nexters/landlords-server/issues/20)) ([f69c564](https://github.com/Nexters/landlords-server/commit/f69c56487ffb9f161990286e30bdf80b2de4fc9b))

### [1.5.2](https://github.com/Nexters/landlords-server/compare/v1.5.1...v1.5.2) (2020-07-24)


### Bug Fixes

* **rooms:** 방 크롤링 예외처리 추가 ([#19](https://github.com/Nexters/landlords-server/issues/19)) ([085ebe3](https://github.com/Nexters/landlords-server/commit/085ebe38b3b49e9cc15095007f12a7de50a79eea))

### [1.5.1](https://github.com/Nexters/landlords-server/compare/v1.5.0...v1.5.1) (2020-07-24)

## [1.5.0](https://github.com/Nexters/landlords-server/compare/v1.4.0...v1.5.0) (2020-07-22)


### Features

* **oauth:** 구글 oauth2 인증을 통한 회원 인증 기능 추가 ([#17](https://github.com/Nexters/landlords-server/issues/17)) ([024dbc7](https://github.com/Nexters/landlords-server/commit/024dbc7d0c2c9bc1ff8a3b9533b138fd02e60f36))

## [1.4.0](https://github.com/Nexters/landlords-server/compare/v1.3.0...v1.4.0) (2020-07-20)


### Features

* **dabang:** 다방 공유 url을 통한 api 데이터 크롤링 ([a6e35c7](https://github.com/Nexters/landlords-server/commit/a6e35c7cd24840214892c14f555ee02a79e7e7aa))

## [1.3.0](https://github.com/Nexters/landlords-server/compare/v1.2.1...v1.3.0) (2020-07-18)


### Features

* **room:** 방 매물 정보 crud 추가 ([80c3e44](https://github.com/Nexters/landlords-server/commit/80c3e4402c0091aa392021175b4daa265761392f))

### [1.2.1](https://github.com/Nexters/landlords-server/compare/v1.2.0...v1.2.1) (2020-07-16)

## [1.2.0](https://github.com/Nexters/landlords-server/compare/v1.1.2...v1.2.0) (2020-07-14)


### Features

* **database:** 데이터베이스 연동 및 테스트 ([7558c6b](https://github.com/Nexters/landlords-server/commit/7558c6b8b36d873e5e739a8a254e39f92508d7fe))

### [1.1.2](https://github.com/Nexters/landlords-server/compare/v1.1.1...v1.1.2) (2020-07-13)

### [1.1.1](https://github.com/Nexters/landlords-server/compare/v1.1.0...v1.1.1) (2020-07-10)


### Bug Fixes

* **release:** 도커 이미지 버전 추가 ([0f8d390](https://github.com/Nexters/landlords-server/commit/0f8d39011e232cdbe32846d86043da760aea7f6a))
* **release:** 릴리즈 상세설명 줄 바꿈 버그 수정, docker 레포 경로 수정 ([d662796](https://github.com/Nexters/landlords-server/commit/d662796035f6adda89f6a9ac7673d1baa9783776))
* **version:** 다음 릴리즈 버전 계산 스크립트 추가 ([ebf1e95](https://github.com/Nexters/landlords-server/commit/ebf1e95a0e9cb19355ee10aa828d773a3c6036cc))

## 1.1.0 (2020-07-05)


### Features

* application 초기 작업 (health check, function test) ([68d158b](https://github.com/Nexters/landlords-server/commit/68d158b76f8313da75b17b57d29411a51313de8c))
* **docker:** docker container build  추가 ([c4d8bbf](https://github.com/Nexters/landlords-server/commit/c4d8bbf46ee9c1d0c3aec4860ef27b29c9cba905))
* **github-action:** release, changelog, lint & test 추가 ([1e83304](https://github.com/Nexters/landlords-server/commit/1e83304eee371a3b8ce6561ea74602dbf0a6f85b))
* **test, lint:** 테스트, 정적 분석, 코드 컨벤션 관리를 위한 도구 추가 ([d437063](https://github.com/Nexters/landlords-server/commit/d4370639b7406fc745d390fd19fd5376510c7e21))


### Bug Fixes

* **release:** github action yaml 문법 실패 수정 ([b797571](https://github.com/Nexters/landlords-server/commit/b797571578a23876c0e3337d343f42df6a0efac3))
