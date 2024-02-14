from datasets import load_dataset
import  gluonts

dataset = load_dataset('Salesforce/cloudops_tsf', 'azure_vm_traces_2017')
print(dataset)

DatasetDict({
    train_test: Dataset({
        features: ['start', 'target', 'item_id', 'feat_static_cat', 'feat_static_real', 'past_feat_dynamic_real'],
        num_rows: 17568
    }),
    pretrain: Dataset({
        features: ['start', 'target', 'item_id', 'feat_static_cat', 'feat_static_real', 'past_feat_dynamic_real'],
        num_rows: 159472
    })
})