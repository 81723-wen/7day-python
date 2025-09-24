#Day2 合同编号生成器
with open('contracts.txt','w',encoding='utf-8') as f:
    for i in range(1,11):
        contract_id = f'2025-HT-{i:03d}'
        f.write(contract_id + '\n')   #每行一个编号
        print(contract_id)

print('10份合同编号已写入contracts.txt, 请验收～')
