#Day2 合同编号生成器
num = int(input('生成几份？请输入数字：'))

with open('contracts.txt','w',encoding='utf-8') as f:
    for i in range(1,num + 1):        # 1到 num(含)
        contract_id = f'2025-HT-{i:03d}'
        f.write(contract_id + '\n')   #每行一个编号
        print(contract_id)

print('10份合同编号已写入contracts.txt, 请验收～')


