# Raw Dataset Inspection

Fecha de inspeccion: 2026-08-04

Esta inspeccion revisa estructura, columnas y conteos iniciales sin modificar los archivos crudos.

## Resumen

| Dataset | Archivo | Formato | Filas/aristas | Nodos unicos | Self-loops | Duplicados dirigidos | Nota |
|---|---|---|---:|---:|---:|---:|---|
| `string_human_physical_v12` | `9606.protein.physical.links.v12.0.txt.gz` | gzip text, space-delimited | 1477610 | 18767 | 0 | 0 | Physical protein associations for Homo sapiens; entries appear as directed/symmetric rows and should be deduplicated for undirected PPI tasks. |
| `openbiolink2020_hq_directed` | `HQ_DIR.zip` | zip archive | 9302547 | 184732 | Not checked yet | Not checked yet | Archive contains 24 files. Parsed split-like TSV files for preliminary entity/relation counts. |
| `biogrid_human` | `BIOGRID-ORGANISM-LATEST.tab3.zip` | zip archive, BioGRID Tab3 | 1404902 | 29502 | 9333 | Not checked yet | Human candidate files: BIOGRID-ORGANISM-Homo_sapiens-5.0.260.tab3.txt |

## string_human_physical_v12

- Archivo: `9606.protein.physical.links.v12.0.txt.gz`
- Tamano: `8954065` bytes
- SHA-256: `1ca87209a93cf7685e9c2997fbcfbfc69fedc6a803ccc1df917318a651df0823`
- Archivos internos: 1 compressed table
- Columnas: protein1; protein2; combined_score

### Muestra

```text
9606.ENSP00000000233	9606.ENSP00000257770	311
9606.ENSP00000000233	9606.ENSP00000226004	161
9606.ENSP00000000233	9606.ENSP00000434442	499
9606.ENSP00000000233	9606.ENSP00000262455	531
9606.ENSP00000000233	9606.ENSP00000303145	499
```

## openbiolink2020_hq_directed

- Archivo: `HQ_DIR.zip`
- Tamano: `109387184` bytes
- SHA-256: `3836c5bca14816ae60e44a5d29f2f893ed566081ea48aaf665ccc26ec746cf55`
- Archivos internos: HQ_DIR/; HQ_DIR/graph_files/; HQ_DIR/graph_files/ALL_nodes.csv; HQ_DIR/graph_files/edges.csv; HQ_DIR/graph_files/edges_list.csv; HQ_DIR/graph_files/graph_props.json; HQ_DIR/graph_files/ids_no_mapping.tsv; HQ_DIR/graph_files/nodes.csv; HQ_DIR/graph_files/nodes_list.csv; HQ_DIR/graph_files/stats.txt; HQ_DIR/graph_files/TN_edges.csv; HQ_DIR/graph_files/TN_edges_list.csv; HQ_DIR/graph_files/tn_ids_no_mapping.tsv; HQ_DIR/graph_files/TN_nodes.csv; HQ_DIR/graph_files/TN_nodes_list.csv; HQ_DIR/graph_files/tn_stats.txt; HQ_DIR/train_test_data/; HQ_DIR/train_test_data/negative_test_sample.csv; HQ_DIR/train_test_data/negative_train_sample.csv; HQ_DIR/train_test_data/negative_val_sample.csv; HQ_DIR/train_test_data/removed_test_nodes.csv; HQ_DIR/train_test_data/removed_val_nodes.csv; HQ_DIR/train_test_data/test_nodes.csv; HQ_DIR/train_test_data/test_sample.csv; HQ_DIR/train_test_data/train_sample.csv; HQ_DIR/train_test_data/train_val_nodes.csv; HQ_DIR/train_test_data/val_sample.csv
- Columnas: Triples inferred as subject; relation; object for split files

### Archivos internos y conteos

- `HQ_DIR/graph_files/ALL_nodes.csv`: 184765 lineas
- `HQ_DIR/graph_files/edges.csv`: 4778683 lineas
- `HQ_DIR/graph_files/edges_list.csv`: 32 lineas
- `HQ_DIR/graph_files/graph_props.json`: 7 lineas
- `HQ_DIR/graph_files/ids_no_mapping.tsv`: 100125 lineas
- `HQ_DIR/graph_files/nodes.csv`: 184667 lineas
- `HQ_DIR/graph_files/nodes_list.csv`: 7 lineas
- `HQ_DIR/graph_files/stats.txt`: 37 lineas
- `HQ_DIR/graph_files/TN_edges.csv`: 621268 lineas
- `HQ_DIR/graph_files/TN_edges_list.csv`: 5 lineas
- `HQ_DIR/graph_files/tn_ids_no_mapping.tsv`: 65309 lineas
- `HQ_DIR/graph_files/TN_nodes.csv`: 21380 lineas
- `HQ_DIR/graph_files/TN_nodes_list.csv`: 5 lineas
- `HQ_DIR/graph_files/tn_stats.txt`: 6 lineas
- `HQ_DIR/train_test_data/negative_test_sample.csv`: 218892 lineas
- `HQ_DIR/train_test_data/negative_train_sample.csv`: 4311578 lineas
- `HQ_DIR/train_test_data/negative_val_sample.csv`: 208672 lineas
- `HQ_DIR/train_test_data/removed_test_nodes.csv`: 20 lineas
- `HQ_DIR/train_test_data/removed_val_nodes.csv`: 17 lineas
- `HQ_DIR/train_test_data/test_nodes.csv`: 101200 lineas
- `HQ_DIR/train_test_data/test_sample.csv`: 183009 lineas
- `HQ_DIR/train_test_data/train_sample.csv`: 4192002 lineas
- `HQ_DIR/train_test_data/train_val_nodes.csv`: 184749 lineas
- `HQ_DIR/train_test_data/val_sample.csv`: 188394 lineas

### Relaciones mas frecuentes

- `GENE_EXPRESSED_ANATOMY`: 2917406
- `GENE_GENE`: 1508169
- `GENE_REACTION_GENE`: 739393
- `GENE_CATALYSIS_GENE`: 575750
- `GENE_BINDING_GENE`: 544832
- `GENE_GO`: 408225
- `DRUG_BINDING_GENE`: 357779
- `GENE_DRUG`: 347235
- `GENE_PHENOTYPE`: 322006
- `GENE_PATHWAY`: 271618

### Muestra

`HQ_DIR/graph_files/ALL_nodes.csv`

```text
CL:0000000	ANATOMY
CL:0000001	ANATOMY
CL:0000003	ANATOMY
CL:0000005	ANATOMY
CL:0000006	ANATOMY
```

`HQ_DIR/graph_files/edges.csv`

```text
CL:0000001	IS_A	CL:0000010		UBERON
CL:0000003	IS_A	CL:0000000		UBERON
CL:0000005	IS_A	CL:0000057		UBERON
CL:0000006	IS_A	CL:0000101		UBERON
CL:0000006	IS_A	CL:0000197		UBERON
```

`HQ_DIR/graph_files/edges_list.csv`

```text
DRUG_BINDING_GENE
GENE_EXPRESSED_ANATOMY
DRUG_PHENOTYPE
GENE_BINDING_GENE
GENE_OVEREXPRESSED_ANATOMY
```

`HQ_DIR/graph_files/graph_props.json`

```text
{
    "DIRECTED": "True",
    "EDGE_TYPES": "['DRUG_BINDING_GENE', 'GENE_EXPRESSED_ANATOMY', 'DRUG_PHENOTYPE', 'GENE_BINDING_GENE', 'GENE_OVEREXPRESSED_ANATOMY', 'DRUG_CATALYSIS_GENE', 'GENE_DIS', 'GENE_ACTIVATION_GENE', 'DIS_PHENOTYPE', 'GENE_REACTION_GENE', 'GENE_INHIBITION_GENE', 'DIS_DRUG', 'DRUG_ACTIVATION_GENE', 'DRUG_REACTION_GENE', 'GENE_CATALYSIS_GENE', 'GENE_GENE', 'GENE_BINDACT_GENE', 'GENE_EXPRESSION_GENE', 'GENE_UNDEREXPRESSED_ANATOMY', 'DRUG_EXPRESSION_GENE', 'GENE_DRUG', 'GENE_PHENOTYPE', 'GENE_PATHWAY', 'DRUG_PREDBIND_GENE', 'GENE_PTMOD_GENE', 'DRUG_BINDINH_GENE', 'DRUG_INHIBITION_GENE', 'DRUG_BINDACT_GENE', 'GENE_BINDINH_GENE', 'GENE_GO', 'PART_OF', 'IS_A']",
    "NODE_NAMESPACES": "['PUBCHEM.COMPOUND', 'HP', 'GO', 'DOID', 'NCBIGENE', 'MULTI']",
    "NODE_TYPES": "['DRUG', 'GENE', 'ANATOMY', 'PHENOTYPE', 'DIS', 'PATHWAY', 'GO']",
```

`HQ_DIR/graph_files/ids_no_mapping.tsv`

```text
ENSEMBL:ENSP00000297564	DRUG_BINDING_GENE
ENSEMBL:ENSP00000339377	DRUG_BINDING_GENE
ENSEMBL:ENSP00000342381	DRUG_BINDING_GENE
ENSEMBL:ENSP00000305059	DRUG_BINDING_GENE
ENSEMBL:ENSP00000346142	DRUG_BINDING_GENE
```

`HQ_DIR/graph_files/nodes.csv`

```text
CL:0000000	ANATOMY
CL:0000001	ANATOMY
CL:0000003	ANATOMY
CL:0000005	ANATOMY
CL:0000006	ANATOMY
```

`HQ_DIR/graph_files/nodes_list.csv`

```text
DRUG
GENE
ANATOMY
PHENOTYPE
DIS
```

`HQ_DIR/graph_files/stats.txt`

```text
Edge Type	Node1 Type	Node2 Type	Nr edges	Nr edges no mapping	Nr edges below cutoff	Edges coverage	Duplicated edges	Nr edges return direction	Nr edges after mapping (final nr)	Nr nodes1 no mapping	Nr nodes2 no mapping	Nr nodes1	Nr nodes2	nodes1 coverage	nodes2 coverage
DRUG_BINDING_GENE	DRUG	GENE	4599374	947944	3516205	0.793897169484369	3606	0	178895	0	2282	287640	10313	1.0	0.7787258799573354
GENE_EXPRESSED_ANATOMY	GENE	ANATOMY	5867702	2407334	2483456	0.589731380359807	347352	0	1466711	40502	0	59166	308	0.3154514417063854	1.0
DRUG_PHENOTYPE	DRUG	PHENOTYPE	309849	124329	0	0.5987432588131638	104996	0	89096	0	4354	1556	5868	1.0	0.25800954328561687
GENE_BINDING_GENE	GENE	GENE	325410	23514	170149	0.927740389047663	258	142788	285318	359	468	12666	13208	0.9716564029685772	0.9645669291338582
```

`HQ_DIR/graph_files/TN_edges.csv`

```text
DOID:0050214	DIS_DRUG	PUBCHEM.COMPOUND:10630		DrugCentral
DOID:0050214	DIS_DRUG	PUBCHEM.COMPOUND:39765		DrugCentral
DOID:0050214	DIS_DRUG	PUBCHEM.COMPOUND:441290		DrugCentral
DOID:0050214	DIS_DRUG	PUBCHEM.COMPOUND:47319		DrugCentral
DOID:0050214	DIS_DRUG	PUBCHEM.COMPOUND:5311399		DrugCentral
```

`HQ_DIR/graph_files/TN_edges_list.csv`

```text
GENE_EXPRESSED_ANATOMY
GENE_OVEREXPRESSED_ANATOMY
DIS_PHENOTYPE
GENE_UNDEREXPRESSED_ANATOMY
DIS_DRUG
```

`HQ_DIR/graph_files/tn_ids_no_mapping.tsv`

```text
ENSEMBL:ENSG00000251495	GENE_EXPRESSED_ANATOMY
ENSEMBL:ENSG00000266775	GENE_EXPRESSED_ANATOMY
ENSEMBL:ENSG00000264112	GENE_EXPRESSED_ANATOMY
ENSEMBL:ENSG00000275265	GENE_EXPRESSED_ANATOMY
ENSEMBL:ENSG00000180662	GENE_EXPRESSED_ANATOMY
```

`HQ_DIR/graph_files/TN_nodes.csv`

```text
CL:0000015	ANATOMY
CL:0000083	ANATOMY
CL:0000169	ANATOMY
CL:0000738	ANATOMY
CL:0002092	ANATOMY
```

`HQ_DIR/graph_files/TN_nodes_list.csv`

```text
GENE
ANATOMY
DIS
PHENOTYPE
DRUG
```

`HQ_DIR/graph_files/tn_stats.txt`

```text
Edge Type	Node1 Type	Node2 Type	Nr edges	Nr edges no mapping	Nr edges below cutoff	Edges coverage	Duplicated edges	Nr edges return direction	Nr edges after mapping (final nr)	Nr nodes1 no mapping	Nr nodes2 no mapping	Nr nodes1	Nr nodes2	nodes1 coverage	nodes2 coverage
GENE_EXPRESSED_ANATOMY	GENE	ANATOMY	2893316	2107817	563730	0.2714874559156345	60132	0	329181	39729	0	56208	270	0.29317890691716486	1.0
GENE_OVEREXPRESSED_ANATOMY	GENE	ANATOMY	343320	53814	202239	0.8432541069556099	26975	0	129294	11056	0	28569	98	0.6130071056039763	1.0
DIS_PHENOTYPE	DIS	PHENOTYPE	906	469	116	0.48233995584988965	24	0	300	333	0	631	356	0.4722662440570523	1.0
GENE_UNDEREXPRESSED_ANATOMY	GENE	ANATOMY	307885	54943	150607	0.8215470061873752	29787	0	133767	13579	0	31658	97	0.5710720828858424	1.0
```

`HQ_DIR/train_test_data/negative_test_sample.csv`

```text
NCBIGENE:80314	GENE_EXPRESSED_ANATOMY	UBERON:0003603		0	GENERATED
NCBIGENE:84236	GENE_EXPRESSED_ANATOMY	UBERON:0006076		0	GENERATED
NCBIGENE:5923	GENE_EXPRESSED_ANATOMY	UBERON:0000399	gold quality	0	Bgee
NCBIGENE:85865	GENE_CATALYSIS_GENE	NCBIGENE:3799		0	GENERATED
NCBIGENE:5728	GENE_GO	GO:0099548		0	GENERATED
```

`HQ_DIR/train_test_data/negative_train_sample.csv`

```text
PUBCHEM.COMPOUND:11733088	DRUG_CATALYSIS_GENE	NCBIGENE:8467		0	GENERATED
NCBIGENE:84808	GENE_EXPRESSED_ANATOMY	UBERON:0004640		0	GENERATED
NCBIGENE:57526	GENE_EXPRESSED_ANATOMY	UBERON:0003550		0	GENERATED
NCBIGENE:442891	GENE_PATHWAY	REACTOME:R-HSA-6811434		0	GENERATED
NCBIGENE:151449	GENE_EXPRESSED_ANATOMY	UBERON:0004901		0	GENERATED
```

`HQ_DIR/train_test_data/negative_val_sample.csv`

```text
NCBIGENE:5226	GENE_UNDEREXPRESSED_ANATOMY	UBERON:0000997	high quality	0	Bgee
DOID:8339	DIS_PHENOTYPE	HP:0031298		0	GENERATED
NCBIGENE:51765	GENE_GENE	NCBIGENE:89953		0	GENERATED
NCBIGENE:56244	GENE_EXPRESSED_ANATOMY	UBERON:4300135		0	GENERATED
NCBIGENE:84063	GENE_GENE	NCBIGENE:80323		0	GENERATED
```

`HQ_DIR/train_test_data/removed_test_nodes.csv`

```text
PUBCHEM.COMPOUND:44455619
GO:0009034
DOID:10081
PUBCHEM.COMPOUND:501050
PUBCHEM.COMPOUND:14327023
```

`HQ_DIR/train_test_data/removed_val_nodes.csv`

```text
PUBCHEM.COMPOUND:19770286
PUBCHEM.COMPOUND:44336602
PUBCHEM.COMPOUND:57398710
PUBCHEM.COMPOUND:10445946
PUBCHEM.COMPOUND:54292863
```

`HQ_DIR/train_test_data/test_nodes.csv`

```text
HP:0010872	PHENOTYPE
GO:0003896	GO
HP:0004607	PHENOTYPE
UBERON:0025261	ANATOMY
PUBCHEM.COMPOUND:160326	DRUG
```

`HQ_DIR/train_test_data/test_sample.csv`

```text
NCBIGENE:125988	GENE_EXPRESSED_ANATOMY	UBERON:0001882	gold quality	1	Bgee
NCBIGENE:78999	GENE_EXPRESSED_ANATOMY	UBERON:0002369	gold quality	1	Bgee
NCBIGENE:28988	GENE_BINDING_GENE	NCBIGENE:22941	922	1	STRING
NCBIGENE:29924	GENE_CATALYSIS_GENE	NCBIGENE:551	900	1	STRING
NCBIGENE:84775	GENE_EXPRESSED_ANATOMY	UBERON:0001950	gold quality	1	Bgee
```

`HQ_DIR/train_test_data/train_sample.csv`

```text
NCBIGENE:11200	GENE_PHENOTYPE	HP:0009919		1	HPO
NCBIGENE:2649	GENE_EXPRESSED_ANATOMY	UBERON:0000059	gold quality	1	Bgee
NCBIGENE:534	GENE_EXPRESSED_ANATOMY	UBERON:0000467	gold quality	1	Bgee
NCBIGENE:2036	GENE_BINDING_GENE	NCBIGENE:5295	900	1	STRING
NCBIGENE:51195	GENE_UNDEREXPRESSED_ANATOMY	CL:0000738	high quality	1	Bgee
```

`HQ_DIR/train_test_data/train_val_nodes.csv`

```text
GO:0051505	GO
PUBCHEM.COMPOUND:10199303	DRUG
PUBCHEM.COMPOUND:157838	DRUG
UBERON:0025261	ANATOMY
PUBCHEM.COMPOUND:10698567	DRUG
```

`HQ_DIR/train_test_data/val_sample.csv`

```text
NCBIGENE:56922	GENE_EXPRESSED_ANATOMY	UBERON:0002081	gold quality	1	Bgee
NCBIGENE:4007	GENE_EXPRESSED_ANATOMY	UBERON:0001870	gold quality	1	Bgee
NCBIGENE:10144	GENE_UNDEREXPRESSED_ANATOMY	UBERON:0002038	high quality	1	Bgee
NCBIGENE:2049	GENE_REACTION_GENE	NCBIGENE:1949	928	1	STRING
NCBIGENE:5888	GENE_EXPRESSED_ANATOMY	UBERON:0000160	gold quality	1	Bgee
```

## biogrid_human

- Archivo: `BIOGRID-ORGANISM-LATEST.tab3.zip`
- Tamano: `186886894` bytes
- SHA-256: `5f6973cc35e59ad90416600f56194ac7d262628b0e20341940060174c5f93e9b`
- Archivos internos: 98 organism files
- Columnas: #BioGRID Interaction ID; Entrez Gene Interactor A; Entrez Gene Interactor B; BioGRID ID Interactor A; BioGRID ID Interactor B; Systematic Name Interactor A; Systematic Name Interactor B; Official Symbol Interactor A; Official Symbol Interactor B; Synonyms Interactor A; Synonyms Interactor B; Experimental System; Experimental System Type; Author; Publication Source; Organism ID Interactor A; Organism ID Interactor B; Throughput; Score; Modification; Qualifications; Tags; Source Database; SWISS-PROT Accessions Interactor A; TREMBL Accessions Interactor A; REFSEQ Accessions Interactor A; SWISS-PROT Accessions Interactor B; TREMBL Accessions Interactor B; REFSEQ Accessions Interactor B; Ontology Term IDs; Ontology Term Names; Ontology Term Categories; Ontology Term Qualifier IDs; Ontology Term Qualifier Names; Ontology Term Types; Organism Name Interactor A; Organism Name Interactor B

### Tipos de interaccion

- `physical`: 1385452
- `genetic`: 19450

### Muestra

```text
103	6416	2318	112315	108607	-	-	MAP2K4	FLNC	JNKK|JNKK1|MAPKK4|MEK4|MKK4|PRKMK4|SAPKK-1|SAPKK1|SEK1|SERK1|SKK1	ABP-280|ABP280A|ABPA|ABPL|FLN2|MFM5|MPD4	Two-hybrid	physical	Marti A (1997)	PUBMED:9006895	9606	9606	Low Throughput	-	-	-	-	BIOGRID	P45985	-	NP_003001|NP_001268364	Q14315	Q59H94	NP_001120959|NP_001449	-	-	-	-	-	-	Homo sapiens	Homo sapiens
117	84665	88	124185	106603	-	-	MYPN	ACTN2	CMD1DD|CMH22|MYOP|RCM4	CMD1AA	Two-hybrid	physical	Bang ML (2001)	PUBMED:11309420	9606	9606	Low Throughput	-	-	-	-	BIOGRID	Q86TC9	A0A087WX60	NP_001243197|NP_001243196|NP_115967	P35609	Q59FD9|F6THM6	NP_001094|NP_001265272|NP_001265273	-	-	-	-	-	-	Homo sapiens	Homo sapiens
183	90	2339	106605	108625	-	-	ACVR1	FNTA	ACTRI|ACVR1A|ACVRLK2|ALK2|FOP|SKR1|TSRI	FPTA|PGGT1A|PTAR2	Two-hybrid	physical	Wang T (1996)	PUBMED:8599089	9606	9606	Low Throughput	-	-	-	-	BIOGRID	Q04771	D3DPA4	NP_001104537|NP_001096	P49354	-	NP_002018	-	-	-	-	-	-	Homo sapiens	Homo sapiens
278	2624	5371	108894	111384	-	-	GATA2	PML	DCML|IMD21|MONOMAC|NFE1B	MYL|PP8675|RNF71|TRIM19	Two-hybrid	physical	Tsuzuki S (2000)	PUBMED:10938104	9606	9606	Low Throughput	-	-	-	-	BIOGRID	P23769	-	NP_001139134|NP_116027|NP_001139133	P29590	-	NP_150250|NP_150253|NP_150252|NP_150247|NP_150241|NP_150242|NP_150243|NP_002666|NP_150249	-	-	-	-	-	-	Homo sapiens	Homo sapiens
418	6118	6774	112038	112651	RP4-547C9.3	-	RPA2	STAT3	REPA2|RP-A p32|RP-A p34|RPA32	ADMIO|APRF|HIES	Two-hybrid	physical	Kim J (2000)	PUBMED:10875894	9606	9606	Low Throughput	-	-	-	-	BIOGRID	P15927	B4DUL2	NP_001342057|NP_002937|NP_001284487|NP_001342058|NP_001273005	P40763	-	NP_644805|NP_003141|NP_001356447|NP_001356443|NP_001371920|NP_001371913|NP_001371917|NP_001356445|NP_001356446|NP_998827|NP_001371915|NP_001371914|NP_001356442|NP_001371918|NP_001371919|NP_001371921|NP_001371922|NP_001371916|NP_001356448|NP_001356449|NP_001356441	-	-	-	-	-	-	Homo sapiens	Homo sapiens
```
