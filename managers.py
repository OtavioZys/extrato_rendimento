# from prompt_toolkit.key_binding.bindings.named_commands import self_insert
#
# from apps.extrato.getters import get_extrato
# import apps.extrato.models
#
#
# class ClienteManager:
#     def get_cliente(self):
#         data_list = get_extrato()
#         print(data_list)
#         data1_list = data_list['value']
#         print(data1_list)
#         cliente_list = []
#
#         for value in data1_list:
#             dadoCliente = self_insert(
#                 id=value['id'],
#                 cliente=value['cliente'],
#             )
#             cliente_list = [dadoCliente]
#         print(cliente_list)
#         return cliente_list
#
#
# class ResumoExtratoManager:
#     def get_resumo(self):
#         data_list = get_extrato()
#         data1_list = data_list['value']
#         data2_list = data1_list['cliente']
#         print(data2_list)
#         data3_list = data2_list['resumo']
#         print(data3_list)
#         resumo_list = []
#
#         for resumo in data3_list:
#             dadoResumo = self(
#                 id=resumo['id'],
#                 cliente=resumo['cliente'],
#                 saldoAnterior=resumo['saldoAnterior'],
#                 saldoAtual=resumo['saldoAtual'],
#                 saldoBloqueado=resumo['saldoBloqueado'],
#                 saldoDisponivel=resumo['saldoDisponivel'],
#                 valorBloqueado=resumo['valorBloqueado'],
#                 limite=resumo['limite'],
#             )
#             resumo_list = [dadoResumo]
#         print(resumo_list)
#         return resumo_list
#
#
# class ItemManager:
#     def get_itens(self):
#         data_list = get_extrato()
#         data1_list = data_list['value']
#         data2_list = data1_list['cliente']
#         data3_list = data2_list['itens']
#         data4_list = data3_list['historico']
#         print(data4_list)
#         itens_list = []
#         historico_list = []
#
#         for itens in data3_list:
#             dadoItem = self.objects(
#                 id=itens['id'],
#                 cliente=itens['cliente'],
#                 historico=itens['historico'],
#                 natureza=itens['natureza'],
#                 dataLancto=itens['dataLancto'],
#                 nrDocumento=itens['nrDocumento'],
#                 cpfCnpj=itens['cpfCnpj'],
#                 nomeContraparte=itens['nomeContraparte'],
#                 agenciaContraparte=itens['agenciaContraparte'],
#                 contaContraparte=itens['contaContraparte'],
#                 valor=itens['valor'],
#                 tipoOperacao=itens['tipoOperacao'],
#             )
#             itens_list = [dadoItem]
#
#         for historico in data4_list:
#             dadoHistorico = self(
#                 codigo=historico['codigo'],
#                 descricao=historico['descricao'],
#                 complemento=historico['complemento'],
#                 categoria=historico['categoria'],
#             )
#             historico_list = [dadoHistorico]
#
#         bulk_itens = [itens_list, historico_list]
#         print(bulk_itens)
#         return bulk_itens
