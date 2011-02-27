function(doc) { 
    emit(doc.infos.constituency.country.code, { 
        'id': doc._id,  
        'group': doc.infos.group.abbreviation,  
        'first': doc.infos.name.first,  
        'last': doc.infos.name.last
    }); 
}
