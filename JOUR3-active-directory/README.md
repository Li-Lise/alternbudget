# 📁 Chapitre 3 — Active Directory, ITSM & Analyse Réseau

> **DEVLABCYB** · Laboratoire simulé d'administration systèmes et cybersécurité  
> Scénario fictif : DEVLABCYB, prestataire IT pour CGI / La Banque Postale  
> Clients VIP simulés : Safran · Thales · Capgemini

---

## 🗒️ Note — Du "Jour" au "Chapitre"

Les premières itérations de ce laboratoire utilisaient la nomenclature **Jour 1, Jour 2...** inspirée des défis de type *#100DaysOfCode*.

Ce choix a été abandonné au profit de **Chapitre**, pour deux raisons :

- **Structurer le lab** de façon plus lisible et modulaire — chaque chapitre couvre un domaine cohérent, pas nécessairement réalisé en une seule session.
- **Faire preuve d'humilité** face à la diversité des thèmes abordés : Active Directory, Docker, ITSM, analyse réseau, détection d'anomalies... Un "jour" suggère une maîtrise complète. Un "chapitre" assume qu'on est en train d'apprendre, et c'est précisément l'honnêteté que ce lab veut incarner.

---

## 🏗️ Environnement Technique

### Forêt Active Directory

| Domaine | Rôle | Machine |
|---|---|---|
| `aerospace-alternants.local` | Domaine racine | ROOT-DC01 — Windows Server 2022 |
| `safran.aerospace-alternants.local` | Domaine enfant | SAFRAN-DC01 — Windows Server 2022 |

- **NetBIOS** : `AEROSPACE-ALTER`
- **OU principales** : `Alternants_Actifs`, `Comptes_Suspendus`, `Comptes_Services`, `Quarantaine_Securite`, `Alternants_Sortants`
- **Compte de service** : `svc-glpi` (OU=Comptes_Services)

### Serveurs

| Machine | OS | Rôle |
|---|---|---|
| ROOT-DC01 | Windows Server 2022 | Contrôleur de domaine principal |
| SAFRAN-DC01 | Windows Server 2022 | Contrôleur de domaine enfant |
| Ubuntu-SRV01 | Ubuntu 22.04 | Stack Docker — iTop, GLPI, MID Server |

### Stack ITSM (Docker — Ubuntu-SRV01)

| Outil | Version | Port | Statut |
|---|---|---|---|
| **iTop** | 3.2.2 | 8070 | ✅ Opérationnel — Auth LDAP via `svc-glpi` |
| **GLPI** | latest | — | ✅ Opérationnel |
| **ServiceNow MID Server** | PDI free tier | — | ⚠️ Up/Validating — limité PDI |
| **Zabbix** | — | — | 📋 Placeholder Ch3 → intégration Ch4 |

### Outils d'analyse

| Outil | Usage dans ce chapitre |
|---|---|
| **Wireshark / tshark** | Capture réseau — export `.pcapng` — INC-008 |
| **PowerShell 5.1** | Scripts d'administration AD — INC-001 à INC-007 |
| **Get-WinEvent** | Analyse des journaux Windows — EventID 4625 |

---

## 📋 Incidents Traités

| ID | Titre | Statut | Script |
|---|---|---|---|
| INC-001 | Déverrouillage de compte AD | ✅ Validé | `INC-001_Unlock-Account.ps1` |
| INC-002 | Réinitialisation de mot de passe AD | ✅ Validé | `INC-002_Reset-Password.ps1` |
| INC-003 | Détection et suppression d'admins non autorisés | ✅ Validé | `INC-003_detect_domainadmin.ps1` |
| INC-004 | Offboarding — Désactivation + déplacement + retrait groupes | ✅ Validé | `INC-004_Offboarding.ps1` |
| INC-005 | Création de compte AD + vérification | ✅ Validé | `INC-005_NewADUser.ps1` |
| INC-006 | Audit AD complet + export CSV | ✅ Validé | `INC-006_Audit-AD-Complet_Export-CSV.ps1` |
| INC-007 | Détection d'anomalies — EventID 4625 + placeholder Zabbix | ✅ Validé | `INC-007_Detect-FailedLogons.ps1` |
| INC-008 | Capture réseau Wireshark + rapport d'analyse | ✅ Validé | `INC-008_Rapport.ps1` + `.pcapng` + `.docx` |

---

## 📂 Structure du Chapitre

```
Ch3/
├── README.md
├── Scripts/
│   ├── INC-001_Unlock-Account.ps1
│   ├── INC-002_Reset-Password.ps1
│   ├── INC-003_detect_domainadmin.ps1
│   ├── INC-004_Offboarding.ps1
│   ├── INC-005_NewADUser.ps1
│   ├── INC-006_Audit-AD-Complet_Export-CSV.ps1
│   ├── INC-007_Detect-FailedLogons.ps1
│   └── INC-008_Rapport.ps1
├── Rapports/
│   ├── INC-001_2026-03-22_03-13-31.txt
│   ├── INC-002_2026-03-22_02-20-12.txt
│   ├── INC-003_2026-03-22_05-59-42.txt
│   ├── INC-004_K.malikaoui_20260405_225626.txt
│   ├── INC-005_v.moreau_20260406_014020.txt
│   ├── INC-006_Audit-AD_2026-04-06_17-32.csv
│   ├── INC-006_Rapport.md
│   ├── INC-007_LOG_20260406_2329.txt
│   └── INC-008_Rapport_Wireshark.docx
└── Captures/
    └── INC-008_capture_AD_DEVLABCYB.pcapng
```

---

## 🔍 Ce que ce chapitre démontre

### Administration Active Directory
Gestion du cycle de vie des comptes : création, modification, désactivation, déplacement entre OU, retrait de groupes. Détection d'élévations de privilèges non autorisées.

### Scripting PowerShell orienté production
Chaque script génère un rapport horodaté dans `C:\Rapports\`, inclut une gestion d'erreurs, et suit une convention de nommage cohérente. Les commandes sont expliquées avant exécution — approche Socratique volontaire.

### Analyse de journaux Windows
Exploitation de `Get-WinEvent` sur EventID 4625 (échecs d'authentification) pour détecter des comportements anormaux. Préparation à l'intégration Zabbix (Ch4).

### Analyse réseau avec Wireshark
Capture de trafic réel sur l'interface du DC, identification des protocoles actifs (NBNS, DNS, TLS, DHCP, NTP, ARP), analyse des flux vers ServiceNow et Microsoft Azure, export `.pcapng` et rapport documenté.

### Documentation technique
Chaque incident produit un rapport lisible : `.txt` horodaté pour les scripts PS1, `.csv` pour les audits, `.md` pour les synthèses, `.docx` pour les analyses réseau.

---

## 🧭 Lien avec le parcours global

```
Ch1 — VoIP & REST API (3CX)
Ch2 — Ticketing & Docker (GLPI + MariaDB)
Ch3 — Active Directory, ITSM & Analyse Réseau  ← vous êtes ici
Ch4 — Monitoring & Détection (Zabbix, Wazuh, Arkime, OpenSearch)
Ch5 — Cloud & Automatisation (M365, Azure, Proxmox)
Ch6 — Sécurité Réseau (VLANs, FortiAnalyzer, SNMP)
Ch7 — MLOps & IAOps (à définir)
```

---

*DEVLABCYB — Laboratoire personnel · Scénario fictif à des fins pédagogiques uniquement*  
*Toutes les données, noms et configurations sont simulés.*
