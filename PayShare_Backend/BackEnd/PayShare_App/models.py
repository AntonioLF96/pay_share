from django.db import models

# Create your models here.


class User(models.Model):
    code = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    fiscalCode = models.CharField(max_length=250)
    birthDate = models.DateField()
    birthPlace = models.CharField(max_length=250)
    residence = models.CharField(max_length=250)
    smartContractList = models.CharField(max_length=250) #TODO
    extensions = models.CharField(max_length=250)
        
    
class Transaction(models.Model):
    idUser = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    recipientCode = models.CharField(max_length=250)
    #recipientId: models.ForeignKey(User, on_delete=models.CASCADE)  #BlockChain

    
    def __str__(self):
        return f"Transaction id:{self.idTransaction},\nidUser:{self.idUser},\nrecipientCode:{self.recipientCode}"
    

    
class Bancomat(models.Model):
    budget = models.CharField(max_length=250)
    extensions = models.CharField(max_length=250)

 
class SmartContract(models.Model):
    idBancomat =  models.ForeignKey(Bancomat, on_delete=models.CASCADE)
    userIdList = models.CharField(max_length=250) #TODO
    transactionIdList = models.CharField(max_length=250) #TODO
    finalTransactionId =  models.ForeignKey(Transaction, on_delete=models.CASCADE)
    extensions = models.CharField(max_length=250)
   
class BancomatSmartContract(models.Model):
    idBancomat =  models.ForeignKey(Bancomat, on_delete=models.CASCADE)
    idSmartContract =  models.ForeignKey(SmartContract, on_delete=models.CASCADE)
    bEnd = models.BooleanField()


class Group(models.Model):
    name = models.CharField(max_length=250)
    userList = models.CharField(max_length=250) #TODO
    recipientId = models.ForeignKey(User, on_delete=models.CASCADE)
    smartContractId = models.ForeignKey(SmartContract, on_delete=models.CASCADE)
    bEnd = models.CharField(max_length=250)
    dStart = models.CharField(max_length=250)
    dateEnd = models.DateField()
    bFinalObjcet = models.BooleanField()
    importObject = models.CharField(max_length=250)
    bSplit = models.BooleanField
    split = models.CharField(max_length=250)
    extensions = models.CharField(max_length=250)




