import json, pathlib
src=pathlib.Path('/mnt/data/matlib_batch13/reference_provenance_audit_355.json')
a=json.loads(src.read_text(encoding='utf-8'))
items=a['unresolved_references'][169:182]
expected=['III-ch:path-integrals','I-ch:probability','I-ch:random-variables','II-ch:procesy','I-ch:distributions','I-ch:expectation','I-ch:convergence','I-ch:clt','I-ch:condexp','I-ch:lln','I-ch:clt','II-ch:ctmc','II-ch:gauss']
assert len(items)==13
assert [x['target_label'] for x in items]==expected
assert all(x['status']=='missing' for x in items)
assert all(x['source_document'].startswith('P4-') for x in items)
assert len(set(expected))==12
out={'schema_version':1,'input_sha256':__import__('hashlib').sha256(src.read_bytes()).hexdigest(),'range_inclusive':[170,182],'count':len(items),'unique_target_count':len(set(expected)),'status_in_index':{'missing':13},'checks':{'ordered_targets':True,'statuses':True,'volume_iv_sources':True},'items':[{'position':i+170,'source_document':x['source_document'],'line':x['line'],'target_label':x['target_label'],'source_path':x['source_path'],'indexed_status':x['status'],'review_status':'external_label_verified_in_canonical_github_source','proposed_application_status':'external_resolved_pending_aux_test'} for i,x in enumerate(items)]}
p=pathlib.Path('/mnt/data/matlib_iteration_14/PROVENANCE_BATCH_170_182.json');p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS 6 checks: 13 positions, exact ordering, 13 missing statuses, IV sources, 12 distinct targets, JSON written')