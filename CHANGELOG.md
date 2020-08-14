# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

### [1.12.5](https://github.com/Nexters/landlords-server/compare/v1.12.4...v1.12.5) (2020-08-14)


### Bug Fixes

* **room, checklist:** 매매, 주거타입 str로 반환, 크롤링 데이터 수정, state를 status로 변경 ([#43](https://github.com/Nexters/landlords-server/issues/43)) ([dd8d103](https://github.com/Nexters/landlords-server/commit/dd8d1030c8eabbf9c455644889d64a5200186889))

### [1.12.4](https://github.com/Nexters/landlords-server/compare/v1.12.3...v1.12.4) (2020-08-12)


### Bug Fixes

* 방 매물 저장, 오타, 체크리스트 nullable 추가 ([#42](https://github.com/Nexters/landlords-server/issues/42)) ([d5f28ea](https://github.com/Nexters/landlords-server/commit/d5f28eaec47c1797d7e2d54e32729333806c2d74))

### [1.12.3](https://github.com/Nexters/landlords-server/compare/v1.12.2...v1.12.3) (2020-08-11)


### Bug Fixes

* **room:** 전용면적, 층, 엘리베이터, 관리비 항목 추가 ([#41](https://github.com/Nexters/landlords-server/issues/41)) ([0533780](https://github.com/Nexters/landlords-server/commit/05337801af279107a593c9257f0e37973d52874c))

### [1.12.2](https://github.com/Nexters/landlords-server/compare/v1.12.1...v1.12.2) (2020-08-10)


### Bug Fixes

* **auth:** get_current_user 버그 수정 ([#40](https://github.com/Nexters/landlords-server/issues/40)) ([d462f2c](https://github.com/Nexters/landlords-server/commit/d462f2cb18e3d6ec45a169875089eeadfc0b33e9))

### [1.12.1](https://github.com/Nexters/landlords-server/compare/v1.12.0...v1.12.1) (2020-08-10)


### Bug Fixes

* **checklist:** 체크리스트 방 계약상태 컬럼 추가 ([#39](https://github.com/Nexters/landlords-server/issues/39)) ([2704b8b](https://github.com/Nexters/landlords-server/commit/2704b8bcb0bd7c9c771c5062c7d52c550119eafc))

## [1.12.0](https://github.com/Nexters/landlords-server/compare/v1.11.5...v1.12.0) (2020-08-10)


### Features

* **token:** oauth 토큰을 검증하여 app token 발급하기 ([#38](https://github.com/Nexters/landlords-server/issues/38)) ([e10cc18](https://github.com/Nexters/landlords-server/commit/e10cc18467cce2e1e8f51c528e8c758738402401))

### [1.11.5](https://github.com/Nexters/landlords-server/compare/v1.11.4...v1.11.5) (2020-08-05)

### [1.11.4](https://github.com/Nexters/landlords-server/compare/v1.11.3...v1.11.4) (2020-08-05)


### Bug Fixes

* **room:** 이미지 컬럼 추가 및 SalesType 반환 ([#35](https://github.com/Nexters/landlords-server/issues/35)) ([d69473a](https://github.com/Nexters/landlords-server/commit/d69473a8c0eee26aa3310d0e446d6191f74d65f3))

### [1.11.3](https://github.com/Nexters/landlords-server/compare/v1.11.2...v1.11.3) (2020-08-04)


### Bug Fixes

* **cookie:** cookie 생성 시 domain 추가 ([#36](https://github.com/Nexters/landlords-server/issues/36)) ([0b41e86](https://github.com/Nexters/landlords-server/commit/0b41e86bc85ed58abc995f3d2e33d03f1ef5ee8b))

### [1.11.2](https://github.com/Nexters/landlords-server/compare/v1.11.1...v1.11.2) (2020-08-02)

### [1.11.1](https://github.com/Nexters/landlords-server/compare/v1.11.0...v1.11.1) (2020-08-02)

## [1.11.0](https://github.com/Nexters/landlords-server/compare/v1.10.0...v1.11.0) (2020-08-02)


### Features

* **cors:** cors 처리 추가 ([b47f2cb](https://github.com/Nexters/landlords-server/commit/b47f2cb8b801cefb8da54bac963d86857a4d3f1b))

## [1.10.0](https://github.com/Nexters/landlords-server/compare/v1.9.2...v1.10.0) (2020-08-02)


### Features

* **token-cookie:** web과 통합을 위한 token 처리 ([ec433bc](https://github.com/Nexters/landlords-server/commit/ec433bce5ac9e68ac97980c5146d843b30252866))

### [1.9.2](https://github.com/Nexters/landlords-server/compare/v1.9.1...v1.9.2) (2020-08-02)


### Bug Fixes

* **rooms:** 방 리소스 유저 연결 및 response 수정 ([dbec589](https://github.com/Nexters/landlords-server/commit/dbec5898d46993d23c84dca2435ab4cfa57c925f))

### [1.9.1](https://github.com/Nexters/landlords-server/compare/v1.9.0...v1.9.1) (2020-07-31)

## [1.9.0](https://github.com/Nexters/landlords-server/compare/v1.8.0...v1.9.0) (2020-07-31)


### Features

* **checklist:** 체크리스트 생성, 응답내역 불러오기 및 체크삭제 api 추가 ([#26](https://github.com/Nexters/landlords-server/issues/26)) ([2faec56](https://github.com/Nexters/landlords-server/commit/2faec561d1678bf3c510bd7942482a92941ff956))

## [1.8.0](https://github.com/Nexters/landlords-server/compare/v1.7.0...v1.8.0) (2020-07-30)


### Features

* **jwk:** jwk 추가 ([913fa1e](https://github.com/Nexters/landlords-server/commit/913fa1e7b7dc79df94826197fc4da6c10d9bf6cf))

## [1.7.0](https://github.com/Nexters/landlords-server/compare/v1.6.3...v1.7.0) (2020-07-30)


### Features

* **deploy:** gcp cloud 자동 배포 추가 ([0e73321](https://github.com/Nexters/landlords-server/commit/0e7332102b89328e02ba0d27755a0b349e90d993))

### [1.6.3](https://github.com/Nexters/landlords-server/compare/v1.6.2...v1.6.3) (2020-07-30)


### Bug Fixes

* **choices:** 페르소나 설문 내역이 없는 경우 list에 none을 담아 반환되는 버그 수정 ([#23](https://github.com/Nexters/landlords-server/issues/23)) ([88429f2](https://github.com/Nexters/landlords-server/commit/88429f2178155a057c61c4acc73ca28f3a6db954))

### [1.6.2](https://github.com/Nexters/landlords-server/compare/v1.6.1...v1.6.2) (2020-07-27)

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
